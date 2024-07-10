import datetime
import os
import shutil
from time import sleep

print("""
      
██████╗  █████╗  ██████╗██╗  ██╗        ██╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝        ██║   ██║██╔══██╗
██████╔╝███████║██║     █████╔╝         ██║   ██║██████╔╝
██╔══██╗██╔══██║██║     ██╔═██╗         ██║   ██║██╔═══╝ 
██████╔╝██║  ██║╚██████╗██║  ██╗        ╚██████╔╝██║     
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝         ╚═════╝ ╚═╝     
                                                         
      """)
print('By Alvaritou6')
sleep(3)
os.system('cls')

origin_path = input('Please enter the path of the folder you want to back up: ')
destiny_path = "C:/Users/alvar/OneDrive/Backs ups"

dtnow = datetime.datetime.now()
name_folder = dtnow.strftime("%d-%m-%Y_%H-%M")
path_folder = os.path.join(destiny_path, name_folder)

def backup():
    print('\nCopying files...')
    try:
        shutil.copytree(origin_path, path_folder)
        print('Backup complete.')
    except NotADirectoryError:
        print('This path contains a file. Please enter a folder path.')

if os.path.exists(origin_path):
    backup()
else:
    print("\nThe path you entered doesn't exists.")
    exit()
