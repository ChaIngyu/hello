import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Asia/Seoul"))
current_datetime = now.strftime("%Y-%m-%d %H:%M")
print(current_datetime)

webhook_url = 'https://hooks.slack.com/services/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'

message = {
    "text": current_datetime
}

requests.post(webhook_url, data=json.dumps(message))