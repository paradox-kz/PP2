from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))
print("UTC:", utc_time)

almaty_time = utc_time.astimezone(ZoneInfo("Asia/Almaty"))
print("Almaty:", almaty_time)
