import re
import math

def find_pattern(equation):
    a = re.search(r'([+-]?\d+)x\^2', equation)
    b = re.search(r"x\^2([+-]?\d*)x", equation)
    if b == None:
        c = re.search(r"x\^2([+-]?\d*)", equation)
    else:
        c = re.search(r'x([+-]?\d+)', equation)

    return [a, b, c]

def find_discriminant (a, b, c):
    discriminant = b**2 - 4*a*c

    return None if discriminant < 0 else discriminant

def solve_the_equation(equation):
    equation = equation.replace(' ', '')
    eq_elements = find_pattern(equation)

    if eq_elements[1] == None and eq_elements[2] == None:
        eq_elements[0] = int(eq_elements[0].group(1))
        eq_elements[1] = 0
        eq_elements[2] = 0

    elif eq_elements[1] == None:
        eq_elements[0] = int(eq_elements[0].group(1))
        eq_elements[1] = 0
        eq_elements[2] = int(eq_elements[2].group(1))

    elif eq_elements[2] == None:
        eq_elements[0] = int(eq_elements[0].group(1))
        eq_elements[1] = int(eq_elements[1].group(1))
        eq_elements[2] = 0

    else:
        eq_elements[0] = int(eq_elements[0].group(1))
        eq_elements[1] = int(eq_elements[1].group(1))
        eq_elements[2] = int(eq_elements[2].group(1))

    discriminant = find_discriminant(eq_elements[0], eq_elements[1], eq_elements[2])

    if discriminant == None:
        print('No solutions')
    else:
        dis = math.sqrt(discriminant)
        sol_1 = (-eq_elements[1] + dis) / (2*eq_elements[0])
        sol_2 = (-eq_elements[1] - dis) / (2*eq_elements[0])
        print(sol_1, sol_2, sep=', ')

if __name__ == '__main__':
    solve_the_equation('3x^2 - 7x + 2')