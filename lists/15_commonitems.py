'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to find common elements in two lists

'''

def common_items(list1, list2):
       """
        description:
            This program to find common elements between two lists"
        parameters:
            list1,list2:
        return:
            Return lst of common elements
    """
       return list(set(list1) & set(list2))

# Example usage
print(common_items([1, 2, 3], [3, 4, 5]))  # Output: [3]
