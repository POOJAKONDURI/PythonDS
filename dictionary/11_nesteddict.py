
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to form nested dictionary from 1d 

'''

lst = {1,2,3,4}
nested_dict = {}
current = nested_dict
for item in lst:
    current[item] = {}
    current = current[item]
print(nested_dict)