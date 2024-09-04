
'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to print unique values

'''

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_values = set(val for dic in data for val in dic.values())

print("Unique Values:", unique_values)
