'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to check if file exists

'''

import subprocess

command = "dir"  # Use "dir" for Windows


process = subprocess.run(command, shell=True, check=True)

# Print the command output
print(process)
