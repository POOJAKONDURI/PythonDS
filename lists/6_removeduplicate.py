'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to remove duplictaes

'''

def remove_duplicates(lst):
      """
        description:
            This program to remove duplicates"
        parameters:
            lst : list of duplicate elements
        return:
            Returns list without duplicates
    """


      return list(set(lst))

# Example usage
print(remove_duplicates([1, 2, 3, 2, 1, 4]))  # Output: [1, 2, 3, 4]
