"""Create decorator logger. The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.

Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function.

For example

print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo
"""


def logger(func):
    name = func.__name__
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]

    def inner_func(*args, **kwargs):
        msg = f'Executing of function {name} with arguments'
        all_arg = ''
        all_kwg = ''
        for arg in args[len(argnames):]:
            all_arg = all_arg + ' ' + str(arg) + ','
        for kw in kwargs:
            all_kwg = all_kwg + ' ' + str(kwargs[kw]) + ','
        print((msg + all_arg + all_kwg)[:-1] + '...')
        return func(*args, **kwargs)

    return inner_func


@logger
def concat(*args, **kwargs):
    res = ''
    for n in args:
        res = res + str(n)
    for i in kwargs:
        res = res + str(kwargs[i])
    return (res)


@logger
def print_arg(arg):
    print(arg)


@logger
def sum(a, b):
    return a + b


print(concat(1))

print(concat('first string', second = 2, third = 'second string'))

print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))

dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}
concat(**dict_args)

print(sum(2,3))

print_arg(2)