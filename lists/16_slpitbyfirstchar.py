'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to split by first char

'''

from collections import defaultdict

def split_by_first_char(words):

       """
        description:
            This program to find common elements between two lists"
        parameters:
            list1,list2:
        return:
            Return lst of common elements
    """
       result = defaultdict(list)
       for word in words:
         result[word[0]].append(word)
       return dict(result)

print(split_by_first_char(['apple', 'banana', 'pear', 'apricot', 'blueberry']))  



