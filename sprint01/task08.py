"""Convert a certain expression like 2+3 to expression in a postfix notation.

The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
devision (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].

[execution time limit] 4 seconds (py)

[input] array.string expression

An array of tokes of a valid expression in the standard notation.

[output] array.string

Tokens of the expression in the postfix notation."""

OPERATORS = set(['+', '-', '*', '/', '(', ')', '%'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 3}


def toPostFixExpression(e):
    stack = []
    output = []
    for ch in e:
        if ch not in OPERATORS:
            output.append(ch)
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output


print(toPostFixExpression(["2",
                           "+",
                           "3"]))

print(toPostFixExpression(["20",
                           "+",
                           "3",
                           "*",
                           "(",
                           "5",
                           "*",
                           "4",
                           ")"]))

print(toPostFixExpression(["(",
                           "(",
                           "(",
                           "1",
                           "+",
                           "2",
                           ")",
                           "*",
                           "3",
                           ")",
                           "+",
                           "6",
                           ")",
                           "/",
                           "(",
                           "2",
                           "+",
                           "3",
                           ")"]))