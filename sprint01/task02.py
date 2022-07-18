"""Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example

"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters)

[output] boolean

"""


def isPalindrome(str):
    chars = [[chr(165 + i), 0] for i in range(180)]
    for c in str:
        chars[ord(c) - 65][1] += 1
    chars = list(filter(lambda x: x[1] != 0, chars))
    mid_idx = None
    for i in range(len(chars)):
        if chars[i][1] % 2 == 1:
            if mid_idx is not None:
                return False
            mid_idx = i
    mid_idx = mid_idx or 0
    tail = ""
    for i in range(len(chars)):
        if i == mid_idx:
            continue
        tail += chars[i][0] * (chars[i][1] // 2)

    return True


print(isPalindrome("abb"))
print(isPalindrome("trueitrue"))
print(isPalindrome("23332"))
print(isPalindrome("trueistrue"))
print(isPalindrome("123123"))
print(isPalindrome("12312"))
print(isPalindrome("A"))
print(isPalindrome("qqqrrrwww"))
print(isPalindrome("qqqrrr"))
