
'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to remove element from tuple

'''



my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)  # Convert tuple to list
my_list.remove(2)  
my_tuple = tuple(my_list)  
print(my_tuple)  
