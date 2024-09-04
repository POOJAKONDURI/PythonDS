'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to check list of files in directory

'''

import os

# Accept the directory path from the user
directory_path = input("Enter the directory path: ")

# List all files in the directory
if os.path.exists(directory_path):
    files = os.listdir(directory_path)
    print("Files in the directory:")
    for file in files:
        print(file)
else:
    print("Directory does not exist.")
