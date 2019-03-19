import os

cwd = os.getcwd()  # get current working directory
print(cwd)

os.chdir('C:\python_program')  #change directory
files_Direc = (os.listdir('.')) #get all files and directory from folder
for i in files_Direc:
    print (i)
