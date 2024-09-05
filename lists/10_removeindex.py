'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to remove 1st 4th 5th

'''


def remove_elements(lst):
     """
        description:
            This program to remove certain items"
        parameters:
            lst:
        return:
            Returns lst without 1st , 4th, 5th
    """
     return lst[1:4]
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
