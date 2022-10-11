# -*- coding: utf-8 -*-
"""
Author: Nikhil Kumar G
This program is used to test the classifyTriangle program's function used for determining the type of triangle

"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right angled triangle.','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right angled triangle.','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral triangle.','1,1,1 should be equilateral')

    def testNotAtriangle(self):
        self.assertEqual(classifyTriangle(10,4,3),'Not a triangle.','10,4,3 is not a triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(7,4,5),'Scalene triangle.','7,4,5 is a scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

