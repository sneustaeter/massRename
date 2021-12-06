# massRename.py
# Author: Saxon Neustaeter
# Date: 12/03/2021
# Description: Simple script to rename all files of certain type in directory
import string, random, os
import tkinter as tk
from tkinter import filedialog

# My Functions
def generateFileNames(count):
    len = 5
    usableChars = string.ascii_letters + string.digits
    namelist = []
    item = ""
    i = 0
    while i < count:
        for x in range(len+1):
            item = item + random.choice(usableChars)
        #print(item)
        namelist.append(item)
    print(namelist)

os.system("cls")

balls = input("Press ENTER to select the target directory: ")

# Directory selection using tkinter
root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory()

# print(file_path)

# Loop over given directory
filecount = 0
for filename in os.scandir(file_path):
    if filename.is_file():
        #print(filename.name)
        filecount = filecount + 1

#print(filecount)

generateFileNames(6)

        
        
        