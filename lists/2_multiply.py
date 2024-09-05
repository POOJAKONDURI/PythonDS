
'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to multiply list items

'''


def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

print(multiply_list([1, 2, 3, 4])) 
