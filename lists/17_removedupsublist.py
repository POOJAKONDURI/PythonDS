'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to split by first char

'''

def remove_duplicates_lists(lst):
       """
        description:
            This program to remove duplicates of sublist"
        parameters:
            lst :
        return:
            Return non duplicate sublist in a list
    """
       result = []
       for sublist in lst:
         if sublist not in result:
            result.append(sublist)
       return result
print(remove_duplicates_lists([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))

