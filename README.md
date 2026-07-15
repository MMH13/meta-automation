# Facebook + Instagram Automation Hub

Standalone hub that posts to Facebook Pages and Instagram Business accounts
via the Meta Graph API (v23.0). No third-party scheduler, no WordPress
dependency.

## Files

| File | Purpose |
|---|---|
| `accounts.json` | Credentials: app id/secret, long-lived user token, one entry per Facebook Page (page token + linked IG account). **Never commit/share.** |
| `meta_mcp_server.py` | MCP server, registered as `meta` in `~/.mcp.json`. Tools: `list_accounts`, `test_connection`, `refresh_accounts`, `fb_post`, `fb_post_photo`, `fb_list_posts`, `fb_delete_post`, `ig_post_image`, `ig_post_carousel`, `ig_post_reel`, `ig_list_media`, `ig_account_info`, `insights`, `graph_request` (raw passthrough). |
| `meta_cli.py` | Queue runner: `python meta_cli.py run-queue [--dry-run]`, `list-queue`. |
| `queue.json` | Scheduled-post queue (see format in `meta_cli.py` docstring). |
| `scripts/run-queue.ps1` | Task Scheduler wrapper for the queue (logs to `queue-run.log`). |

## Key facts

- Every tool takes an optional `account` arg — a key from `accounts.json`
  (default: `zelobiz`). Slugs: zelobiz, sporting-saga-tv, health-daily, ...
- **Page tokens never expire** (derived from a long-lived user token). If they
  are ever invalidated (password change, secret reset with token invalidation),
  redo the Graph API Explorer token grant and re-run the setup exchange.
- **Facebook scheduling is native**: `fb_post(..., schedule="2026-07-14T09:00")`
  (10 min – 75 days ahead). **Instagram has no native API scheduling** — put IG
  posts in `queue.json` and let Task Scheduler run `run-queue.ps1` every 15 min.
- **Instagram requires**: a Business/Creator IG account linked to the Facebook
  Page. Only `health-daily` (`health_daily13`) is linked so far. After linking
  a new one in Page settings, run the `refresh_accounts` tool.
- IG image URLs must be **public https** (any publicly hosted image works).
  JPEG is safest; some PNGs are rejected.
- App is in **Live mode** (switched 2026-07-13; privacy policy URL:
  zelobiz.com/privacy-policy/). **Never switch back to Development mode** —
  dev-mode apps create posts the API calls "published" but that are invisible
  to everyone without an app role. After posting, verify the permalink loads
  logged-out.

## Setup history

- 2026-07-13: app 1807992553343847 created by user; short-lived token exchanged
  for long-lived (user token expires ~60 days, page tokens permanent);
  16 pages discovered; hub built and connection-verified.
