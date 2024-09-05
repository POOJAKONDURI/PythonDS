'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to see el which are common in two lists

'''

import itertools

def all_permutations(lst):
     """
        description:
            This program to give permutations of list"
        parameters:
            lst:
        return:
            Returns permutations of lst
    """
     return list(itertools.permutations(lst))

print(all_permutations([1, 2, 3]))  
