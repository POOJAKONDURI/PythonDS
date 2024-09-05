
'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to find unique sorted words

'''

# Example of sorting unique words
def unique_sorted_words(s):
    words = s.split(", ")
    unique_words = sorted(set(words))
    return ", ".join(unique_words)


def main():
      """
        description:
            This program to give sorted words
        parameters:
            s : 
        return:
            Returns unique sorted words
    """
      print("Unique sorted words:", unique_sorted_words("red, white, black, red, green, black"))
    
if __name__ == "__main__":
    main()


