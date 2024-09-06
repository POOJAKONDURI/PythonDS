
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to display histogram of list

'''





def create_histogram(lst):
    
 """
        description:
            This program display histogram of integers"
        parameters:
            lst : integers 
        return:
            Returns histogram
    """
 for value in lst:
        print('*' * value)

# Test the function
create_histogram([3, 7, 1, 5])
