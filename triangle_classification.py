# -*- coding: utf-8 -*-
"""
@author: Nikhil Kumar G

This program is used to write a function called classify_triangle() that takes
three  parameters : a, b, and c.
The three parameters represent the lengths of the sides of a triangle.
The function returns a string that specifies whether the triangle is scalene, isosceles,
equilateral, right triangle and if it cannot be a triangle then it returns 'Not a triangle'.

"""

print('Please enter the values for a, b and c: ')
x=int(input())
y=int(input())
z=int(input())


def classify_triangle(a_s,b_s,c_s):
    """
        Function to classify triangles
    """
    if a_s+b_s>c_s and b_s+c_s>a_s and c_s+a_s>b_s:
        if a_s==b_s and b_s==c_s:
            return 'Equilateral triangle'
        elif a_s==b_s or b_s==c_s or a_s==c_s:
            return 'Isosceles triangle.'
        elif a_s**2+b_s**2==c_s**2 or b_s**2+c_s**2==a_s**2 or c_s**2+a_s**2==b_s**2:
            return 'Right angled triangle'
        else:
            return 'Scalene triangle'
    else:
        return 'Not a triangle'

classify_triangle(x,y,z)
