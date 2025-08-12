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