'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to smallest of list

'''

def count_matching_strings(strings):

     """
        description:
            This program gives count of strings which has len graeater than 2 and same character in first and last index"
        parameters:
            strings:
        return:
            Returns string with len>2 and same charecter in start and end 
    """

     count = 0
     for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
     return count

print(count_matching_strings(['abc', 'xyz', 'aba', '1221']))  
