import time
import os
import re
import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)

# Define source folder

print("")
print("UPDATE FINDER 1.2")
print("")
print("================================================================================")
print('WARNING: Put sign " before and after directory path and use forward slash /')
print("================================================================================")
rar_path = str(input("Enter path to the directory with WinRAR.exe: "))
source_folder = str(input("Input the path of Directory with unzipped drivers: "))
dstdir = str(input("Input the path of Directory where will be located Archives with updates: "))

# Define a Period with updates
start_year = int(input("Enter period start Year (yyyy): "))
start_month = int(input("Enter period start Month (m): "))
print("=================================================================================")
print("WARNING: Dates from End Period month and older will not be included to te results")
print("=================================================================================")
end_year = int(input("Enter period end Year (yyyy): "))
end_month = int(input("Enter period end Month (m): "))

start_time_tuple = (start_year, start_month, 1, 0, 0, 0, 0, 0, 0)
start_timestamp = time.mktime(start_time_tuple)

end_time_tuple = (end_year, end_month, 1, 0, 0, 0, 0, 0, 0)
end_timestamp = time.mktime(end_time_tuple)

# Create a set which includes updated directories
updated_folders = set()

# Find all directories with updates and put them to the set
for top, dirs, files in os.walk(source_folder):
    for nm in files:
        if ((end_timestamp > os.path.getmtime(os.path.join(top, nm)) > start_timestamp) or (end_timestamp > os.path.getmtime(top) > start_timestamp)) and not re.match(r"(.+)nfo$", nm):
            if ((os.path.dirname(top)).replace("\\", '/') in updated_folders) or ((os.path.dirname(os.path.dirname(top))).replace("\\", '/') in updated_folders) or ((os.path.dirname(os.path.dirname(os.path.dirname(top)))).replace("\\", '/') in updated_folders):
                break
            else:
                for i in updated_folders:
                    if top == os.path.dirname(i) or top == os.path.dirname(os.path.dirname(i)) or top == os.path.dirname(os.path.dirname(os.path.dirname(i))):
                        updated_folders.remove(i)
                    else:
                        break
                updated_folders.add(top.replace("\\", '/'))


# Delete advertisement from directories with updates
for i in updated_folders:
    if os.path.exists(i + "/www.SamLab.ws.url"):
        os.remove(i + "/www.SamLab.ws.url")
        print(i + "/www.SamLab.ws.url " + " Advertisement is found and DELETED!")

# Create a folder for RAR archives
if not os.path.exists(dstdir):
    os.mkdir(dstdir)

print(str(len(updated_folders)) + " archives with updated data will be created...")

# Create RAR archives
k = 0
for i in updated_folders:
    k += 1
    source = str(i)
    rar_name = source[(len(source_folder)+1):].replace("/", "_")
    dst = dstdir + os.sep + rar_name + '.rar'
    rar = rar_path + "/WinRAR.exe u -as -dh -ep1 {0} {1}".format(dst, source)
    if os.system(rar)==0:
        print(str(k) + " from " + str(len(updated_folders)) + " RAR is created in " + str(dst))
    else:
        print('RAR creating is FAILED')

print ("PROCESS FINISHED")
