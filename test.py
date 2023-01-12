from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours = 7))
date = datetime.now(tz=tz)
date_el = date.ctime().split(' ')

time_formated = f"{date_el[2]} {date_el[1]} {date_el[4]} {date_el[3]}"
print(time_formated)