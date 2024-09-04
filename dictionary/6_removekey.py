
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to remove key

'''

d = {'apple': 40, 'banana': 10, 'cherry': 30, 'date': 20}
key_to_remove = 'banana'
if key_to_remove in d:
    del d[key_to_remove]

print("Updated Dictionary:", d)
