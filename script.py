import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Asia/Seoul"))
current_datetime = now.strftime("%Y-%m-%d %H:%M")
print(current_datetime)

