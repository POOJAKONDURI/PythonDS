'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to know frozenset

'''


my_frozenset = frozenset([1, 2, 3, 4, 5])

# Trying to add or remove items from a frozenset will raise an error
print("Frozenset:", my_frozenset)

# Frozenset operations like union and intersection can still be performed
set1 = {3, 4, 5, 6}
union = my_frozenset.union(set1)
print("Union with frozenset:", union)
