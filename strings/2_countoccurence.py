'''

    @Author:pooja
    @Date:05-09-2024
    @last modified by:pooja
    @last modified time:05-09-2024
    @title:program to count frquency of char

'''


def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


sample_string = "google.com"
print(char_frequency(sample_string))

