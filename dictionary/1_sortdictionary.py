'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to sort dictionary

'''


d = {'a':9,'b':4,'c':8}
res = dict(sorted(d.items(), key = lambda item:item[1]))
print("sorted in ascending",res)
res = dict(sorted(d.items(), key = lambda item:item[1],reverse = True))
print("sorted in descending",res)