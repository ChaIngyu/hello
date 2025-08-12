import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import os

now = datetime.now(ZoneInfo("Asia/Seoul"))
current_datetime = now.strftime("%Y-%m-%d %H:%M")
print(current_datetime)

webhook_url = os.getenv("WEBHOOK_LINK")

message = {
    "text": current_datetime
}

requests.post(webhook_url, data=json.dumps(message))
