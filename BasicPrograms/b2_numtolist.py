'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to find head and tail percentage on flip 

'''

"""
        description:
            This program converts numbers separated by commas to list and tuple"
        parameters:
            numbers: numbers seoarated by commas
        return:
            Returns tuple
    """




numbers = input("Enter comma-separated numbers: ")

# Generate list and tuple
num_list = numbers.split(",")
num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)
