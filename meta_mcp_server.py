"""Meta MCP server — post to Facebook Pages and Instagram via the Graph API.

Accounts are defined in accounts.json next to this file (generated from the
one-time token-exchange setup):
    {
      "default_account": "zelobiz",
      "app_id": "...", "app_secret": "...",
      "long_lived_user_token": "...",
      "accounts": {
        "zelobiz": {"page_id": "...", "page_name": "Zelo Biz",
                     "page_token": "...", "ig_user_id": null, "ig_username": null}
      }
    }

Every tool takes an optional `account` argument (the key from accounts.json).
When omitted, default_account is used. Page tokens derived from a long-lived
user token do not expire. Instagram tools require the page to have a linked
IG Business/Creator account (run refresh_accounts after linking one).
"""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from mcp.server.fastmcp import FastMCP

_HERE = Path(__file__).parent
_ACCOUNTS_FILE = _HERE / "accounts.json"

GRAPH = "https://graph.facebook.com/v23.0"

_conf: dict = json.loads(_ACCOUNTS_FILE.read_text(encoding="utf-8"))
ACCOUNTS: dict = _conf.get("accounts", {})
DEFAULT_ACCOUNT: str = _conf.get("default_account") or next(iter(ACCOUNTS), "")

mcp = FastMCP("meta")


def _cfg(account: str) -> dict:
    name = account or DEFAULT_ACCOUNT
    if name not in ACCOUNTS:
        raise RuntimeError(
            f"Unknown account '{name}'. Configured accounts: {list(ACCOUNTS)}. "
            f"Add it to {_ACCOUNTS_FILE}"
        )
    return ACCOUNTS[name]


def _ig_id(account: str) -> str:
    c = _cfg(account)
    if not c.get("ig_user_id"):
        raise RuntimeError(
            f"Account '{account or DEFAULT_ACCOUNT}' ({c['page_name']}) has no linked "
            "Instagram Business account. Link one in the Facebook Page settings "
            "(Linked accounts -> Instagram), then run refresh_accounts."
        )
    return c["ig_user_id"]


def _api(method: str, endpoint: str, *, account: str = "", params=None,
         payload=None, token: str = "") -> dict:
    tok = token or _cfg(account)["page_token"]
    params = dict(params or {})
    params["access_token"] = tok
    resp = requests.request(method, f"{GRAPH}/{endpoint.lstrip('/')}",
                            params=params, json=payload, timeout=60)
    body = resp.json() if resp.text else {}
    if resp.status_code >= 400:
        err = (body.get("error") or {})
        raise RuntimeError(
            f"Graph API {resp.status_code}: {err.get('message', resp.text[:500])} "
            f"(type={err.get('type')}, code={err.get('code')}, "
            f"subcode={err.get('error_subcode')})"
        )
    return body


def _dump(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def _to_unix(when: str) -> int:
    """ISO-8601 string -> unix timestamp. Naive strings are local time."""
    dt = datetime.fromisoformat(when)
    if dt.tzinfo is None:
        dt = dt.astimezone()
    return int(dt.timestamp())


@mcp.tool()
def list_accounts() -> str:
    """List configured Facebook Pages, their linked Instagram accounts, and the default account key."""
    return _dump({
        "default_account": DEFAULT_ACCOUNT,
        "accounts": {k: {"page": v["page_name"], "page_id": v["page_id"],
                         "instagram": v.get("ig_username")}
                     for k, v in ACCOUNTS.items()},
    })


@mcp.tool()
def test_connection(account: str = "") -> str:
    """Verify the page token works. Returns page name, follower count, and linked IG account."""
    c = _cfg(account)
    page = _api("GET", c["page_id"], account=account,
                params={"fields": "id,name,link,followers_count,fan_count,"
                                  "instagram_business_account{id,username}"})
    return _dump(page)


@mcp.tool()
def refresh_accounts() -> str:
    """Re-discover pages and linked Instagram accounts using the stored long-lived user
    token, and update accounts.json in place (preserves default_account and slugs for
    pages already present). Run this after linking an IG account to a page or creating
    a new page."""
    user_tok = _conf["long_lived_user_token"]
    pages, after = [], None
    while True:
        params = {"fields": "id,name,access_token", "limit": 100}
        if after:
            params["after"] = after
        r = _api("GET", "me/accounts", token=user_tok, params=params)
        pages += r.get("data", [])
        after = (r.get("paging", {}).get("cursors") or {}).get("after")
        if not after or not r.get("data"):
            break

    by_id = {v["page_id"]: k for k, v in ACCOUNTS.items()}
    changes = []
    for p in pages:
        ig = (_api("GET", p["id"], token=p["access_token"],
                   params={"fields": "instagram_business_account{id,username}"})
              .get("instagram_business_account"))
        key = by_id.get(p["id"])
        if key is None:
            key = "".join(ch if ch.isalnum() else "-" for ch in p["name"].lower()).strip("-") or p["id"]
            ACCOUNTS[key] = {"page_id": p["id"], "page_name": p["name"]}
            changes.append(f"added {key}")
        entry = ACCOUNTS[key]
        entry["page_token"] = p["access_token"]
        old_ig = entry.get("ig_username")
        entry["ig_user_id"] = ig["id"] if ig else None
        entry["ig_username"] = ig.get("username") if ig else None
        if entry.get("ig_username") != old_ig:
            changes.append(f"{key}: instagram {old_ig!r} -> {entry.get('ig_username')!r}")

    _conf["accounts"] = ACCOUNTS
    _ACCOUNTS_FILE.write_text(_dump(_conf), encoding="utf-8")
    return _dump({"pages_found": len(pages), "changes": changes or ["none"]})


# ---------------------------------------------------------------- Facebook

@mcp.tool()
def fb_post(message: str, link: str = "", schedule: str = "",
            account: str = "") -> str:
    """Publish a text or link post to the Facebook Page feed.
    link: optional URL to attach (renders a preview card).
    schedule: optional ISO datetime (e.g. 2026-07-14T09:00 local time) to use Facebook's
    native scheduling — must be 10 minutes to 75 days in the future."""
    payload = {"message": message}
    if link:
        payload["link"] = link
    if schedule:
        payload["published"] = False
        payload["scheduled_publish_time"] = _to_unix(schedule)
    r = _api("POST", f"{_cfg(account)['page_id']}/feed", account=account,
             payload=payload)
    return _dump(r)


@mcp.tool()
def fb_post_photo(image: str, caption: str = "", schedule: str = "",
                  account: str = "") -> str:
    """Publish a photo post to the Facebook Page.
    image: either a public https URL or a LOCAL file path (uploaded directly).
    schedule: optional ISO datetime for Facebook's native scheduling."""
    c = _cfg(account)
    data = {"message": caption, "access_token": c["page_token"]}
    if schedule:
        data["published"] = "false"
        data["scheduled_publish_time"] = str(_to_unix(schedule))
    if image.lower().startswith(("http://", "https://")):
        data["url"] = image
        resp = requests.post(f"{GRAPH}/{c['page_id']}/photos", data=data,
                             timeout=120)
    else:
        p = Path(image)
        if not p.is_file():
            raise RuntimeError(f"Image file not found: {image}")
        with p.open("rb") as fh:
            resp = requests.post(f"{GRAPH}/{c['page_id']}/photos", data=data,
                                 files={"source": (p.name, fh)}, timeout=120)
    body = resp.json() if resp.text else {}
    if resp.status_code >= 400:
        err = body.get("error") or {}
        raise RuntimeError(f"Graph API {resp.status_code}: "
                           f"{err.get('message', resp.text[:500])}")
    return _dump(body)


@mcp.tool()
def fb_list_posts(limit: int = 10, include_scheduled: bool = False,
                  account: str = "") -> str:
    """List recent published posts on the Page (or scheduled ones with include_scheduled)."""
    edge = "scheduled_posts" if include_scheduled else "feed"
    r = _api("GET", f"{_cfg(account)['page_id']}/{edge}", account=account,
             params={"fields": "id,message,created_time,scheduled_publish_time,"
                               "permalink_url,is_published",
                     "limit": limit})
    return _dump(r.get("data", []))


@mcp.tool()
def fb_delete_post(post_id: str, account: str = "") -> str:
    """Delete a Page post (also works for cancelling a scheduled post)."""
    return _dump(_api("DELETE", post_id, account=account))


# --------------------------------------------------------------- Instagram

def _ig_wait_ready(container_id: str, account: str, timeout_s: int = 120) -> None:
    """Poll a media container until Meta finishes processing it (needed for video;
    images are usually instant)."""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        st = _api("GET", container_id, account=account,
                  params={"fields": "status_code"})
        code = st.get("status_code")
        if code == "FINISHED":
            return
        if code == "ERROR":
            raise RuntimeError(f"IG container {container_id} failed processing: {st}")
        time.sleep(3)
    raise RuntimeError(f"IG container {container_id} not ready after {timeout_s}s")


def _public_image_url(image: str, account: str) -> str:
    """Return a public https URL for the image. Local paths are uploaded to the
    Facebook Page as an UNPUBLISHED photo (never appears on the page) purely to
    obtain a public CDN URL that Instagram's servers can fetch."""
    if image.lower().startswith(("http://", "https://")):
        return image
    p = Path(image)
    if not p.is_absolute():
        p = _HERE / p
    if not p.is_file():
        raise RuntimeError(f"Image file not found: {image}")
    c = _cfg(account)
    with p.open("rb") as fh:
        resp = requests.post(
            f"{GRAPH}/{c['page_id']}/photos",
            data={"published": "false", "access_token": c["page_token"]},
            files={"source": (p.name, fh)}, timeout=120)
    body = resp.json() if resp.text else {}
    if resp.status_code >= 400:
        raise RuntimeError(f"CDN upload failed {resp.status_code}: "
                           f"{(body.get('error') or {}).get('message', '')[:300]}")
    info = _api("GET", body["id"], account=account, params={"fields": "images"})
    return info["images"][0]["source"]  # largest rendition first


@mcp.tool()
def ig_post_image(image_url: str, caption: str = "", account: str = "") -> str:
    """Publish a single image to Instagram. image_url: a PUBLIC https URL or a
    LOCAL file path (auto-hosted via an unpublished Facebook photo upload).
    Publishes immediately — Instagram has no native scheduling via API; use the
    queue for scheduling."""
    ig = _ig_id(account)
    image_url = _public_image_url(image_url, account)
    c = _api("POST", f"{ig}/media", account=account,
             payload={"image_url": image_url, "caption": caption})
    _ig_wait_ready(c["id"], account)
    r = _api("POST", f"{ig}/media_publish", account=account,
             payload={"creation_id": c["id"]})
    perma = _api("GET", r["id"], account=account, params={"fields": "permalink"})
    return _dump({"media_id": r["id"], "permalink": perma.get("permalink")})


@mcp.tool()
def ig_post_carousel(image_urls: list[str], caption: str = "",
                     account: str = "") -> str:
    """Publish a 2-10 image carousel to Instagram. All URLs must be public https."""
    if not 2 <= len(image_urls) <= 10:
        raise RuntimeError("Carousel needs 2-10 images.")
    ig = _ig_id(account)
    children = []
    for url in image_urls:
        c = _api("POST", f"{ig}/media", account=account,
                 payload={"image_url": url, "is_carousel_item": True})
        children.append(c["id"])
    for cid in children:
        _ig_wait_ready(cid, account)
    parent = _api("POST", f"{ig}/media", account=account,
                  payload={"media_type": "CAROUSEL", "caption": caption,
                           "children": ",".join(children)})
    _ig_wait_ready(parent["id"], account)
    r = _api("POST", f"{ig}/media_publish", account=account,
             payload={"creation_id": parent["id"]})
    return _dump({"media_id": r["id"]})


@mcp.tool()
def ig_post_reel(video_url: str, caption: str = "", cover_url: str = "",
                 account: str = "") -> str:
    """Publish a Reel to Instagram from a public video URL (MP4, 3s-15min).
    Processing can take a while; this waits up to 5 minutes."""
    ig = _ig_id(account)
    payload = {"media_type": "REELS", "video_url": video_url, "caption": caption}
    if cover_url:
        payload["cover_url"] = cover_url
    c = _api("POST", f"{ig}/media", account=account, payload=payload)
    _ig_wait_ready(c["id"], account, timeout_s=300)
    r = _api("POST", f"{ig}/media_publish", account=account,
             payload={"creation_id": c["id"]})
    return _dump({"media_id": r["id"]})


@mcp.tool()
def ig_list_media(limit: int = 10, account: str = "") -> str:
    """List recent Instagram posts with permalink, caption, type, and timestamp."""
    ig = _ig_id(account)
    r = _api("GET", f"{ig}/media", account=account,
             params={"fields": "id,caption,media_type,permalink,timestamp,"
                               "like_count,comments_count",
                     "limit": limit})
    return _dump(r.get("data", []))


@mcp.tool()
def ig_account_info(account: str = "") -> str:
    """Get the linked Instagram account's profile: followers, media count, bio."""
    ig = _ig_id(account)
    r = _api("GET", ig, account=account,
             params={"fields": "id,username,name,biography,followers_count,"
                               "follows_count,media_count,profile_picture_url,website"})
    return _dump(r)


# ---------------------------------------------------------------- generic

@mcp.tool()
def insights(object_id: str, metrics: str, period: str = "",
             account: str = "") -> str:
    """Fetch Graph API insights for a page, post, or IG media/user.
    object_id: page id, post id, IG media id, or IG user id.
    metrics: comma-separated (e.g. 'post_impressions' for FB posts;
    'reach,likes,comments,saved' for IG media; 'reach,follower_count' for IG user).
    period: optional (day|week|days_28|lifetime) — mainly for page/user level."""
    params = {"metric": metrics}
    if period:
        params["period"] = period
    r = _api("GET", f"{object_id}/insights", account=account, params=params)
    return _dump(r.get("data", r))


@mcp.tool()
def graph_request(method: str, endpoint: str, params_json: str = "",
                  payload_json: str = "", account: str = "") -> str:
    """Raw Graph API passthrough for anything not covered by a dedicated tool.
    method: GET|POST|DELETE. endpoint: e.g. 'me/accounts' or '<page-id>/feed'.
    params_json / payload_json: JSON-encoded dicts. Uses the account's page token."""
    r = _api(method.upper(), endpoint, account=account,
             params=json.loads(params_json) if params_json else None,
             payload=json.loads(payload_json) if payload_json else None)
    return _dump(r)


if __name__ == "__main__":
    mcp.run()
