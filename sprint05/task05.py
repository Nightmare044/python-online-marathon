"""Write  the function divide(numerator, denominator) the two input parameters of which are numbers. The function returns the result of dividing two numbers.
 in case of correct data the function should be displayed the corresponding message – "Result is  numerator / denominator"
in the case of division by zero the function should be displayed the corresponding message – "Oops, numerator / denominator, division by zero is error!!!"

in the case of incorrect data the function should be displayed the message – "Value Error! You did not enter a number!"
Note: in the function you must use the "try except" construct.

Function example:
divide(8, 16)        #output:   "Result is 0.5"

divide (5, 0)        #output:   "Oops, 5 / 0 denominator, division by zero is error!!!"

divide_number("25", 5)    #output:   "Value Error! You did not enter a number!"

 divide_number("abc", 9)  #output:    "Value Error! You did not enter a number!" """

def divide(numerator, denominator):
    try:
        return f"Result is {numerator/denominator}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except (ValueError,TypeError):
        return "Value Error! You did not enter a number!"


print(divide(4, 8))
print(divide(-1, 4))
print(divide(8, 0))
print(divide(-8, -2))
print(divide("9", 3))
print(divide("avr", 5))