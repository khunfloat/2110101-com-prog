from datetime import datetime, timezone, timedelta
from os import listdir
from os.path import exists
import os, sys

def up():
    tz = timezone(timedelta(hours = 7))
    date = datetime.now(tz=tz)
    date_el = date.ctime().split(' ')
    time_formated = f"{date_el[2]} {date_el[1]} {date_el[4]} {date_el[3]}"

    root_dir = listdir()
    expr_dir = sorted(list(filter(lambda dir: dir.startswith('0'), root_dir)))
    recent_file = ""

    for dir in expr_dir:
        for file in sorted(listdir(dir)):
            if file.endswith('.py'):
                if os.stat(f"{dir}/{file}").st_size == 0:
                    break
                recent_file = file

    f = open("README.md", "w")

    f.write(f'Last Submit on {recent_file}\\\n{time_formated}\\\n\\\nnpm run up')

    f.close()

    os.system("git add README.md")
    os.system('git commit -m "fix: update README.md by runner.py"')

    os.system("git add .")
    os.system('git commit -m "feat: update new contents"')

    os.system("git push")

def generate():
    directory = input("What directory to generate : ")

    file_list = listdir(f'./{directory}')
    pdf_list = []
    for file in file_list:
        if not exists(f'./{directory}/{file.split(".")[0]}.py'):
            with open(f'./{directory}/{file.split(".")[0]}.py', 'w') as f:
                f.close()

    print("done!")

if __name__== "__main__":

    if sys.argv[1] == "up":
        up()
    elif sys.argv[1] == "generate":
        generate()
    else:
        print("Something was error!")