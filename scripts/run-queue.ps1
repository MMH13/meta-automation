# Runs the Meta post queue. Wire into Windows Task Scheduler, e.g. every 15 min:
#   schtasks /Create /TN "MetaPostQueue" /SC MINUTE /MO 15 /TR "powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\Mamun\fb-ig-automation\scripts\run-queue.ps1"
$env:PYTHONIOENCODING = "utf-8"
python "$PSScriptRoot\..\meta_cli.py" run-queue *>> "$PSScriptRoot\..\queue-run.log"
