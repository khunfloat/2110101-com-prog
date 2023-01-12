import os

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
f.write(f"Last Summit on {recent_file}")
f.close()