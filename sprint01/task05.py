"""Given number n and two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].

Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.

Example

Input:
n = 3, p = [3, 1, 2],  q = [2, 1, 3]

Output:
r = [3, 2, 1]
[input] integer n

length of the permutations

[input] array.integer p

[input] array.integer q

[output] array.integer

permutation r
"""
def findPermutation(n, p, q):
    return [p[q[i]-1] for i in range(n)]

n = 5
p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]
print(findPermutation(n, p, q))