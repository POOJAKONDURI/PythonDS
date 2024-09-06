'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to find symmetric difference

'''

# Sample sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# (elements in either set1 or set2, but not in both)
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference)
