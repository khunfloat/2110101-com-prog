from os import listdir
from os.path import exists

directory = input("What directory to generate : ")

file_list = listdir(f'./{directory}')
pdf_list = []
for file in file_list:
    if not exists(f'./{directory}/{file.split(".")[0]}.py'):
        # pdf_list.append(file.split('.')[0])
        with open(f'./{directory}/{file.split(".")[0]}.py', 'w') as f:
            f.close()

print("done!")