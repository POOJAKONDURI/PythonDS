'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to see el which are common in two lists

'''

def twolstcom(lst1,lst2):
     """
        description:
            This program to return true if el in lst1 is in lst2 "
        parameters:
            lst1 and lst2:
        return:
            Returns True if elements in lst1 are in lst2
    """
     for el in lst1:
        if el in lst2:
            return True
        return False
    
lst1 = [1,2,3,4]
lst2 = [1,9,5]
res = twolstcom(lst1,lst2)
print(res)

