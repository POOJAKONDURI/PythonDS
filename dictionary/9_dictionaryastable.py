
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to form table of dictionary

'''


res = {"one":1,"two":2,"three":3}
print(f"{'Key':<10}{'value':<10}")
print("-"*20)
for key,val in res.items():
    print(f"{key:<10} {val:<10}")

