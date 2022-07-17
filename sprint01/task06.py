"""Nicky and Dev work in a company where each member is given his income in the form of points. On Nicky's birthday, Dev decided to give some of his points as a gift. The number of points Dev is gifting is the total number of visible zeros visible in the string representation of the N points he received this month.

Let's say that Nicky got M points from Dev. By the company law, if M is even and greater than 0, Nicky must give one point to the company. If M is odd, the company gives Nicky one additional point.

Given the number of points N Dev received this month, calculate the number of points Nicky will receive as a gift and return this number in its binary form.

Note: visible zeros are calculated as follows:

0, 6 and 9 contain 1 visible zero each;
8 contains 2 visible zeros;
other digits do not contain visible zeros.
Example

For N = "565", the output should be
Cipher_Zeroes(N) = 10.

There's one visible zero in "565". Since one is odd, the company will give an additional point, so Nicky will receive 2 points.
210 = 102, so the output should be 10.

Input/Output

[input] string N

The number of points Dev received this month.

Constraints:
1 ≤ N ≤ 101000.

[output] integer

The number of points Nicky will receive in the binary representation.
"""
def checkVisibleZeroes(N):
    points = 0
    for i in N:
        if i in "069":
            points += 1
        elif i in "8":
            points += 2

    return points


def companyBonus(M):
    if M > 0 and M % 2 == 0:
        return M - 1
    elif M % 2 != 0:
        return M + 1
    else:
        return M


def decimalToBinary(n):
    return int("{0:b}".format(int(n)))


def Cipher_Zeroes(N):
    zeroes = checkVisibleZeroes(N)
    points = companyBonus(zeroes)
    return decimalToBinary(points)

print(Cipher_Zeroes("565"))
print(Cipher_Zeroes("2628426728"))
print(Cipher_Zeroes("0"))
print(Cipher_Zeroes("8200"))
print(Cipher_Zeroes("4"))
print(Cipher_Zeroes("4900"))
print(Cipher_Zeroes("7481"))