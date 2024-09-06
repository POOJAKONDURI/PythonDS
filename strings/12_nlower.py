'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to convert n chArecters as lowercase

'''

def lowercase_first_n(s, n):

      """
        description:
            This program to gives n charecters as 
        parameters:
            s,sub : 
        return:
            Returns n characters as lowercase
    """
      return s[:n].lower() + s[n:]

def main():
      print("Lowercase first n characters:", lowercase_first_n("HELLO World", 5))

if __name__ == "__main__":
    main()