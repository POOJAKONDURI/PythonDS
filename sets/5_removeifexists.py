'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to remove element if doest it doesnt throw error

'''

my_set = {1, 2, 3, 4, 5}

my_set.discard(3)
print("After discarding 3:", my_set)
my_set.discard(10)
print("After discarding 10 (non-existent):", my_set)