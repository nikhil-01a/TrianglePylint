"""
@author: Nikhil Kumar G

This program is used to write a function called classify_triangle() that takes three  parameters: a, b, and c. The three parameters represent the lengths of the sides 
of a triangle. The function returns a string that specifies whether the triangle is scalene, isosceles, equilateral, right triangle and if it cannot be a triangle then
it returns 'Not a triangle'.

"""

#Function to classify triangles
def classify_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        if a==b and b==c:
            return 'Equilateral triangle.'
        elif a==b or b==c or a==c:
            return 'Isosceles triangle.'
        elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
            return 'Right angled triangle.'
        else:
            return 'Scalene triangle.'
    else:
        return 'Not a triangle.'