import requests
import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os
import gspread
from google.oauth2.service_account import Credentials


now = datetime.now(ZoneInfo("Asia/Seoul"))
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(current_datetime)


webhook_url = os.getenv("WEBHOOK_LINK")

service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
credentials = Credentials.from_service_account_info(
    service_account_info,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
gc = gspread.authorize(credentials)

spreadsheet_url = "https://docs.google.com/spreadsheets/d/116J72CQO0K71rcUU3_qT4RE9mpykDXwKYQ9Eb83qN8A/edit?gid=0#gid=0"
doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet("시트1")

all_rows = worksheet.get_values()[1:]

for i in len(all_rows):
    title, message, start_time, period = all_rows[i]
    start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_dt = start_dt + timedelta(minutes=int(period))
    if(start_dt < now and now < end_dt):
        webhook_message = {
            "text": f"{title} : {message}"
        }
        requests.post(webhook_url, data=json.dumps(webhook_message))
    elif(end_dt <= now):
        worksheet.delete_rows(i+2)






