import os
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours = 7))
date = datetime.now(tz=tz)
date_el = date.ctime().split(' ')
time_formated = f"{date_el[2]} {date_el[1]} {date_el[4]} {date_el[3]}"

root_dir = os.listdir()
expr_dir = list(filter(lambda dir: dir.startswith('0'), root_dir))

recent_file = ""

for dir in expr_dir:
    for file in sorted(os.listdir(dir)):
        if file.endswith('.py'):
            if os.stat(f"{dir}/{file}").st_size == 0:
                break
            recent_file = file

f = open("README.md", "w")
f.write(f"Last Summit on {recent_file}\n{time_formated}")
f.close()

os.system("git add README.md")
os.system('git commit -m "fix: update README.md by runner.py"')

os.system("git add .")
os.system('git commit -m "feat: update new contents"')

os.system("git push")