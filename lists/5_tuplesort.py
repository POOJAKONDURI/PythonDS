'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to sort tuples

'''



def sort_by_last_element(tuples):
     """
        description:
            This program to sort tuple end index"
        parameters:
            tuple: list of tuples
        return:
            Returns smallest num
    """
     return sorted(tuples, key=lambda x: x[-1])

print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])) 
