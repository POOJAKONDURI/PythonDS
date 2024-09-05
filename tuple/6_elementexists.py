'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to check element exists

'''


def check_element_in_tuple(tpl, element):
    for item in tpl:
        if item == element:
            return True
    return False
my_tuple = (1, 2, 3, 4)
print(check_element_in_tuple(my_tuple, 2))  
print(check_element_in_tuple(my_tuple, 5))  
