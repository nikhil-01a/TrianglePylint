# -*- coding: utf-8 -*-
"""
Author: Nikhil Kumar G
This program is used to test the classify_triangle program's
function used for determining the type of triangle.

"""

import unittest

from triangle_classification import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """
        This class is used to define multiple sets of tests as
        functions for the classify_triangle method.
    """

    def test_right_triangle_a(self):
        """
            To test for right angled triangle
        """
        self.assertEqual(classify_triangle(3,4,5),'Right angled triangle','It is a Right triangle')

    def test_right_triangle_b(self):
        """
            To test for right angled triangle
        """
        self.assertEqual(classify_triangle(5,3,4),'Right angled triangle','It is a Right triangle')

    def test_equilateral_triangles(self):
        """
            To test for equilateral triangle
        """
        self.assertEqual(classify_triangle(1,1,1),'Equilateral triangle','it should be equilateral')

    def test_not_a_triangle(self):
        """
            To test if it is a triangle or not
        """
        self.assertEqual(classify_triangle(10,4,3),'Not a triangle','10,4,3 is not a triangle')

    def test_scalene_triangles(self):
        """
            To test for scalene triangle
        """
        self.assertEqual(classify_triangle(7,4,5),'Scalene triangle','7,4,5 is a scalene triangle')

    def test_isosceles_triangles(self):
        """
            To test for isosceles triangle
        """
        self.assertEqual(classify_triangle(2,3,2),'Isosceles triangle','Its an Isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
