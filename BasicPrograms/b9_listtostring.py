

'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to convert lst to string

'''


def concatenate_list_elements(lst):
    """
        description:
            This program concatenates lst elements as string"
        parameters:
            list :
        return:
            Returns string
    
"""
    return ''.join(lst)

# Test the function
print(concatenate_list_elements(['a', 'b', 'c']))  # Output: 'abc'
