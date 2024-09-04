
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to check multiple keys present in keys , 

'''


d = {'apple': 40, 'banana': 10, 'cherry': 30}
keys_to_check = ['apple', 'banana']

if all(key in d for key in keys_to_check):
    print("All keys exist in the dictionary")
else:
    print("Some keys are missing")
