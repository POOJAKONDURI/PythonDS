
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to square values of iteem

'''

# Function to generate dictionary
def generate_square_dict(n):
      """
        description:
            This program gives squared values of items"
        parameters:
            n: value of key till which items squared
        return:
            Returns key and squared values
    """

      return {x: x*x for x in range(1, n+1)}

# Sample usage
n = 5
square_dict = generate_square_dict(n)
print("Generated Dictionary:", square_dict)
