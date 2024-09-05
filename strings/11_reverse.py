'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to reverse string

'''

def reverse_string(s):
    """
        description:
            This program to gives reverse of string
        parameters:
            s : 
        return:
            Returns reversed string
    """
    return s[::-1]


def main():
    print("Reversed string:", reverse_string("hello"))

if __name__ == "__main__":
    main()