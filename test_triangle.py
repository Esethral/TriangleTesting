# -*- coding: utf-8 -*-
#I pledge my honor that I have abided by the Stevens Honor System - Evan Abel
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """Class to define unit tests"""
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_b(self):
        """Tests if Right Triangle A"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_a(self):
        """Test if Right Tirangle B"""
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def test_equilateral_triangles(self):
        """Test if Equilateral Triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_length_triangle_a(self):
        """Test if Lengths are valid A"""
        self.assertEqual(classify_triangle(201, 100, 192), 'InvalidInput', '201 greater than 200')

    def test_length_triangle_b(self):
        """Test if lengths are valid B"""
        self.assertEqual(classify_triangle(-1, 2, 6), 'InvalidInput', '-1 is less than 0')

    def test_integer_input(self):
        """Tests if values are integers"""
        self.assertEqual(classify_triangle('a', 2, 7), 'InvalidInput', 'a is not an int')

    def test_if_triangle(self):
        """Tests if lengths can form a triangle"""
        self.assertEqual(classify_triangle(3, 9, 30), 'NotATriangle', 'Sides cant form a triangle')

    def test_isoceles_triangle(self):
        """Test if Isoceles Triangle"""
        self.assertEqual(classify_triangle(3, 4, 3), 'Isoceles', 'Isoceles triangle')

    def test_scalene_triangle(self):
        """Test if Scalene Triangle"""
        self.assertEqual(classify_triangle(5, 6, 7), 'Scalene', 'Scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
