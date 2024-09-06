'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to display color

'''

"""
        description:
            This program to show days between two dates"
        parameters:
            date1 and date2 :
        return:
            Returns dates between two 
    
"""


from datetime import date

# Define the dates
date_1 = date(2014, 7, 2)
date_2 = date(2014, 7, 11)

# Calculate the difference
difference = date_2 - date_1

# Print the number of days
print(f"{difference.days} days")
