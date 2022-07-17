"""As input data, you have a list of strings.

Write a method double_string() for counting the number of strings from the list,

represented in the form of the concatenation of two strings from this arguments  list"""


def double_string(lista):
    count = 0
    for x in lista:
        if any(x + y in lista for y in lista):
            count += 1
    return count


data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))

data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data))

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))