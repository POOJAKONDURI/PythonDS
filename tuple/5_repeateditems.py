'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to unpack tuple

'''


my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)
repeated_items = set([item for item in my_tuple if my_tuple.count(item) > 1])
print(repeated_items)  
