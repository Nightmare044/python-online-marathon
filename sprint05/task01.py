"""Write  the function day_of_week(day) whose input parameter is a number or string representation of number. The function returns the corresponding day of the week if the input parameter is in the range of 1 to 7, namely

· in the case when the input parameter is 5 the function should be displayed the message – "Friday"
· in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message – "There is no such day of the week! Please try again."
· in the case of incorrect data the function should be displayed the message - "You did not enter a number! Please try again."

Note: in the function you must use the "try except" construct.



Function example:

day_of_week(2)                     # output:   "Tuesday"

day_of_week(11)                     # output:  "There is no such day of the week! Please try again."

day_of_week("Monday")       # output:   "You did not enter a number! Please try again."

"""

def day_of_week(day):
    try:
        day = int(day)
    except ValueError:
        return "You did not enter a number! Please try again."
    if day > 7 or day <= 0:
        return "There is no such day of the week! Please try again."
    if day == 1:
        return "Monday"
    if day == 2:
        return "Tuesday"
    if day == 3:
        return "Wednesday"
    if day == 4:
        return "Thursday"
    if day == 5:
        return "Friday"
    if day == 6:
        return "Saturday"
    if day == 7:
        return "Sunday"


print(day_of_week(5))
print(day_of_week(1))
print(day_of_week(0))
print(day_of_week(-9))
print(day_of_week("Sunday"))
print(day_of_week("6"))
print(day_of_week("9"))