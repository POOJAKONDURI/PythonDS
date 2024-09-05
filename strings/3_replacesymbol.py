
'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to replace first charecter with symbol

'''


def symbtofirstchar(str):
     """
        description:
            This program gives "string with occurence of first character replaced with symbol
        parameters:
            str : 
        return:
            Returns string with occurence of first character replaced with symbol
    """
     res = str[0]
     ans = res
     for letter in str[1:]:
        if res in letter:
            ans += '@'
        else:
            ans += letter
     return ans

str = 'restart'
res = symbtofirstchar(str)
print(res)
