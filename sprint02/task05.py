"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

The formula for calculating the distance between points:
"""

import re
from math import sqrt


def figure_perimetr(st):
    l = [i.split(':') for i in re.split("#[A-Z]{2}", st, 0)[1:]]

    def formula(p1, p2):
        return sqrt(((int(p2[0]) - int(p1[0])) ** 2) + (int(p2[1]) - int(p1[1])) ** 2)

    return sum(formula(l[x], l[y]) for x, y in ((0, 2), (2, 3), (3, 1), (1, 0)))


test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
