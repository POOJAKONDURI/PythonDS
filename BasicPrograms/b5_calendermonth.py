'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to print cal of given month and yr

'''

"""
        description:
            This program prints calender"
        parameters:
            month and  year:
        return:
            Returns calender
    """






import calendar

# Accept month and year from user
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Print the calendar
print(calendar.month(year, month))
