


'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to give character before given character

'''


def string_before_char(s, char):

    """
        description:
            This program to give characters before certain in string
        parameters:
            s,char : 
        return:
            Returns characters before certain in string
    """
    
    return s.rsplit(char, 1)[0]

sample_url = "https://www.w3resource.com/python-exercises"
print(string_before_char(sample_url, '/'))

def main():
    print("String before char:", string_before_char("https://www.w3resource.com/python-exercises", '/'))


if __name__ == "__main__":
    main()