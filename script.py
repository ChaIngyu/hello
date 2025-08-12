from datetime import datetime

now = datetime.now()
current_datetime = now.strftime("%Y-%m-%d %H:%M")
print(current_datetime)