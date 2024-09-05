'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to find max word  of words

'''


# Example of finding the longest word
def longest_word(words):
       """
        description:
            This program to give maximum word among words
        parameters:
            str : 
        return:
            Returns max word among words
    """
    

       return max(len(word) for word in words)


def main():
    words = ["apple", "banana", "cherry", "watermelon"]
    print("Length of longest word:", longest_word(words))

if __name__ == "__main__":
    main()