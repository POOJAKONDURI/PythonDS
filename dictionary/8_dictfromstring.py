
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to form dict from string

'''

rs = "maalim"
ls = {}
for item in rs :
    if item in ls:
        ls[item] += 1
    else:
        ls[item] = 1

print(ls)
