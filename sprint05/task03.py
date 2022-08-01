"""Write  the function solve_quadric_equation(a, b, c) the three input parameters of which are numbers. The function should return
the solution of quadratic equation ax2+bx+c=0, where coefficients a, b, c are input parameters of  the function solve_quadric_equation:

 in case of correct data the function should displayed the corresponding message – "The solution are x1=… and x2=…"

in the case of division by zero the function should displayed the corresponding message – "Zero Division Error"

in the case of incorrect data the function should displayed the message – "Could not convert string to float"
Note: in the function you must use the "try except" construct.



 Function example:

solve_quadric_equation(1, 5, 6)            #output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"

solve_quadric_equation(0, 8, 1)            #output:   "Zero Division Error"

solve_quadric_equation(1,”abc”, 5)       #output:   "Could not convert string to float"

"""

import cmath


def solve_quadric_equation(a, b, c):
    try:
        a = float(a)
        if a == 0:
            return "Zero Division Error"
        b = float(b)
        c = float(c)
    except ValueError:
        return "Could not convert string to float"

    d = b ** 2 - 4 * a * c
    return f"The solution are x1={(-b - cmath.sqrt(d)) / (2 * a)} and x2={(-b + cmath.sqrt(d)) / (2 * a)}"


print(solve_quadric_equation(1, 3, -4))
print(solve_quadric_equation(1, 4, 5))
print(solve_quadric_equation(0, 5, 9))
print(solve_quadric_equation("a", 3, 1))
