'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to find difference between two lists

'''

def list_difference(list1, list2):

      """
        description:
            This program to find difference btw two lsts"
        parameters:
            lst1,lst2:
        return:
            Returns difference
    """
      return list(set(list1) - set(list2))

# Example usage
print(list_difference([1, 2, 3], [2, 4]))  # Output: [1, 3]
