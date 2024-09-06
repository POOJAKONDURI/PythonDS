'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to to check if number in group

'''

def is_value_in_group(value, group):

    
 """
        description:
            This program display True if vakue in group"
        parameters:
            group :
            value :
        return:
            Returns True if value in group
    """
 return value in group

# Test data
print(is_value_in_group(3, [1, 5, 8, 3]))  # True
print(is_value_in_group(-1, [1, 5, 8, 3]))  # False
