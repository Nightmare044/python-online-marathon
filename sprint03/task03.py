"""Create function-generator divisor that should return all divisors of the positive number.
If there are no divisors left function should return None.
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None"""


def divisor(num):
    for x in range(1, num + 1):
        if num / x == int(num / x):
            yield x
    while True:
        yield None


var = divisor(1)
print(next(var))

two = divisor(2)
print(next(two))
print(next(two))
print(next(two))
print(next(two))

two = divisor(62832)
for _ in range(10):
    print(f'{next(two)}, ', end="")
