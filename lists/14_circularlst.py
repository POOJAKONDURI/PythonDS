'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to find if two lsts are circularly identical

'''

def circularly_identical(list1, list2):
    """
        description:
            This program to find if two lsts are circularly identical"
        parameters:
            lst1,lst2:
        return:
            Return True if identical
    """
    return len(list1) == len(list2) and any(list1 == list2[i:] + list2[:i] for i in range(len(list2)))

print(circularly_identical([1, 2, 3], [3, 1, 2])) 
