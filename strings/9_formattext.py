

'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to foramat 

'''

import textwrap
def format_text(text, width=50):
     """
        description:
            This program to give textwrap
        parameters:
            text ,width : 
        return:
            Returns text wrap
    """
     return textwrap.fill(text, width)

def main():
     print("Formatted text:", format_text("This is an example of text that will be wrapped to fit within a certain width."))

if __name__ == "__main__":
     main()