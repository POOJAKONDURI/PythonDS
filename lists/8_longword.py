'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to check word which is longer than n

'''

def longer_words(words, n):

    """
        description:
            This program to see words which are longer than n "
        parameters:
            words : list of words
            n:length
        return:
            Returns list without duplicates
    """

    return [word for word in words if len(word) > n]

print(longer_words(['apple', 'banana', 'pear'], 4))
