'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to find count of substring

'''

def count_substring(s, sub):
     """
        description:
            This program to give sub string count
        parameters:
            s,sub : 
        return:
            Returns sub string count
    """
     return s.count(sub)

def main():
      print("Count substring occurrences:", count_substring("hello world, hello universe", "hello"))

if __name__ == "__main__":
      main()