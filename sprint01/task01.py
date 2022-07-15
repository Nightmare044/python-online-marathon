"""For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers of n, or sums of distinct powers of n.

Your task is to find the kth (1-based) number in this sequence.

Example

For n = 3 and k = 4, the output should be
kthTerm(n, k) = 9.

For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
[3**0] => [1]
[1, 3**1, 3**1 +1] => [1, 3, 4]
[1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
...

The 4th number in this sequence is 9, which is the answer.

Input/Output

[input] integer n

The number to build the sequence by.

Constraints:
2 ≤ n ≤ 30.

[input] integer k

The 1-based index of the number in the sequence.

Constraints:
1 ≤ k ≤ 100.

[output] integer

The kth element of the sequence."""


def f1(n=3, k=9):
    def f2(num, lis):
        for i in lis[:-1]:
            a = num + i
            yield a

    a = []
    i = 0
    while i < k:
        if i in (0, 1):
            a.append(n ** i)
            i += 1
            continue
        num = n ** (i - 1)
        b = f2(num, a)
        for x in b:
            a.append(x)
        a.append(n ** (i))
        i += 1
    return a


def kthTerm(n, k):
    if n not in range(1, 31):
        print('n is out of range')
    if k not in range(1, 101):
        print('k is out of range')
    b = f1(n, 8)
    return b[k - 1]


print(kthTerm(3, 4))
print(kthTerm(3, 7))
print(kthTerm(3, 3))
print(kthTerm(2, 7))
print(kthTerm(4, 3))
print(kthTerm(30, 100))
print(kthTerm(2, 1))
print(kthTerm(15, 50))
print(kthTerm(21, 63))
print(kthTerm(10, 99))

print('='*60)


def kthTerm(n, k):
    my_list = []
    for i in range(7):
        power = n ** i
        if i == 0:
            my_list.append(power)
        else:
            sum_of_powers = [power + j for j in my_list]
            my_list.append(power)
            my_list += sum_of_powers

    return my_list[k - 1]


print(kthTerm(3, 4))
print(kthTerm(3, 7))
print(kthTerm(3, 3))
print(kthTerm(2, 7))
print(kthTerm(4, 3))
print(kthTerm(30, 100))
print(kthTerm(2, 1))
print(kthTerm(15, 50))
print(kthTerm(21, 63))
print(kthTerm(10, 99))
