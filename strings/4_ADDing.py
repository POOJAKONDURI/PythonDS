# Example of modifying string based on condition
'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to add ing or ly

'''



def add_suffix(s):
    """
        description:
            This program gives "string with occurence of first character replaced with symbol
        parameters:
            str : 
        return:
            Returns string with occurence of first character replaced with symbol
    """
    if len(s) >= 3:
        if s.endswith("ing"):
            s += "ly"
        else:
            s += "ing"
    return s

# Sample usage
print(add_suffix("abc"))    
print(add_suffix("string")) 
