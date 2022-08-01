"""Write  the function check_positive(number) whose input parameter is a number. The function checks whether the  set number is positive or negative:

in the case of a positive number the function should be displayed the corresponding message - " You input positive number: input parameter of function";
in the case of a negative parameter the function should be raised the exception of your own class MyError and displayed the corresponding message - "You input negative number: input parameter of function. Try again.";
in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"
Function example:

check_positive (24)      #output:    "You input positive number: 24"

check_positive (-19)     #output:     "You input negative number: -19. Try again."

check_positive ("38")    #output:    "You input positive number: 38"

check_positive ("abc")  #output:     "Error type: ValueError!" """


class MyError(Exception):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def __str__(self):
        return f"You input negative number: {self.number}. Try again."


def check_positive(number):
    try:
        number = float(number)
        if float(number) >= 0:
            return f"You input positive number: {number}"
        else:
            return MyError(number)
    except ValueError:
        return "Error type: ValueError!"


print(check_positive(0.7))
print(check_positive(-19))
print(check_positive(8.9))
print(check_positive(-0.6))
print(check_positive("abs"))
print(check_positive("45"))
print(check_positive("-235"))