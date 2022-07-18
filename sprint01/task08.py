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


print(toPostFixExpression(["2", "+", "3"]))

print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))

print(toPostFixExpression(["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))

print('_'*60)

def converter(arr):
    copy = [i for i in arr]
    i = 97
    for j in range(len(arr)):
        if arr[j].isnumeric():
            copy[j] = chr(i)
            i += 1
    return "".join(copy)


def deConverter(original, postfix):
    copy = list(postfix)
    # print("COPY ", copy)
    numbers = []
    for i in range(len(original)):
        if original[i].isnumeric():
            numbers.append(original[i])

    # print(numbers)

    j = 0
    for k in range(len(copy)):
        if copy[k].isalpha():
            # print(copy[k])
            # print(j)
            copy[k] = numbers[j]
            j += 1

    # print("COPY ", copy)

    return copy


class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.output_string = ""
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while ((not self.isEmpty()) and
                       self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    # this is to pass cases like a^b^c
                    # without if ab^c^
                    # with if abc^^
                    if i == "^" and self.array[-1] == i:
                        break
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        self.output_string = "".join(self.output)


def toPostFixExpression(e):
    alpha = converter(e)
    # print("ALPHA, ", alpha)
    # print('ORIGINAL ', e)

    obj = Conversion(len(alpha))
    obj.infixToPostfix(alpha)
    obj.output_string

    # print("POSTFIX ALPHA ", obj.output_string)

    postfix = deConverter(e, obj.output_string)

    return postfix


print(toPostFixExpression(["2", "+", "3"]))

print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))

print(toPostFixExpression(["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))