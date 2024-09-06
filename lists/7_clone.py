'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to copy lst

'''

def clone_list(lst):
     """
        description:
            This program to copy lst"
        parameters:
            lst : original lst
        return:
            Returns cloned lst
    """


     return lst.copy()
original_list = [1, 2, 3, 4]
cloned_list = clone_list(original_list)
print(cloned_list) 
