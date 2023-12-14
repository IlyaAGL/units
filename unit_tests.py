import unittest
import math
import circle
import rectangle
import square
import triangle

class TestLibrary(unittest.TestCase):
    
    # Square Area and Perimeter
    def test_squareArea(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(13), 169)
        self.assertEqual(square.area(1.5), 2.25)
        self.assertEqual(square.area(123456789), 15241578750190521)
        self.assertEqual(square.area(-1408), "ONLY POSITIVE NUMBERS")
        self.assertEqual(square.area(True), "WRONG ARGUMENT TYPE")
        self.assertEqual(square.area("5"), "WRONG ARGUMENT TYPE")
    
    def test_squarePerimeter(self):
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(13), 52)
        self.assertEqual(square.perimeter(1.5), 6)
        self.assertEqual(square.perimeter(123456789), 493827156)
        self.assertEqual(square.perimeter(-1408), "ONLY POSITIVE NUMBERS")
        self.assertEqual(square.perimeter(True), "WRONG ARGUMENT TYPE")
        self.assertEqual(square.perimeter("5"), "WRONG ARGUMENT TYPE")

    # Triangle Area and Perimeter
    def test_triangleArea(self):
        self.assertEqual(triangle.area(0, 0) ,0)
        self.assertEqual(triangle.area(4, 4) ,8)
        self.assertEqual(triangle.area(4, 1.5) ,3)
        self.assertEqual(triangle.area(123456789,2),123456789)
        self.assertEqual(triangle.area(-18,18),"ONLY POSITIVE NUMBERS")
        self.assertEqual(triangle.area(True,1408),"WRONG ARGUMENT TYPE")
        self.assertEqual(triangle.area("2",1408),"WRONG ARGUMENT TYPE")
    
    def test_trianglePerimeter(self):
        self.assertEqual(triangle.perimeter(0,0,0),"THIS TRIANGLE DOESN'T EXIST")
        self.assertEqual(triangle.perimeter(1,2,2),5)
        self.assertEqual(triangle.perimeter(1.5, 1.5, 1.5), 3)
        self.assertEqual(triangle.perimeter(1,2,3), "THIS TRIANGLE DOESN'T EXIST")
        self.assertEqual(triangle.perimeter(300000,400000,500000),1200000)
        self.assertEqual(triangle.perimeter(True, 1408, 123),"WRONG ARGUMENT TYPE")
        self.assertEqual(triangle.perimeter(118,"1408",321),"WRONG ARGUMENT TYPE")

    # Circle Area and Perimeter
    def test_circleArea(self):
        self.assertEqual(circle.area(0),0)
        self.assertEqual(circle.area(18), 324 * math.pi)
        self.assertEqual(circle.area(1.5), 2.25 * math.pi)
        self.assertEqual(circle.area(123456789),15241578750190521 * math.pi)
        self.assertEqual(circle.area(-1408), "ONLY POSITIVE NUMBERS")
        self.assertEqual(square.area(True), "WRONG ARGUMENT TYPE")
        self.assertEqual(circle.area("15"), "WRONG ARGUMENT TYPE")

    def test_circlePerimeter(self):
        self.assertEqual(circle.perimeter(0),0)
        self.assertEqual(circle.perimeter(18), 36 * math.pi)
        self.assertEqual(circle.perimeter(1.5), 3 * math.pi)
        self.assertEqual(circle.perimeter(123456789),246913578 * math.pi)
        self.assertEqual(circle.perimeter(-1408), "ONLY POSITIVE NUMBERS")
        self.assertEqual(circle.perimeter(True), "WRONG ARGUMENT TYPE")
        self.assertEqual(circle.perimeter("15"), "WRONG ARGUMENT TYPE")

    # Rectangle Area and Perimeter
    def test_rectangleArea(self):
        self.assertEqual(triangle.area(0, 0), 0)
        self.assertEqual(triangle.area(4,4), 8)
        self.assertEqual(triangle.area(1.5, 2), 3)
        self.assertEqual(triangle.area(123456789,2),123456789)
        self.assertEqual(triangle.area(-18,18),"ONLY POSITIVE NUMBERS")
        self.assertEqual(triangle.area(True,1408),"WRONG ARGUMENT TYPE")
        self.assertEqual(triangle.area("2",1408),"WRONG ARGUMENT TYPE")
    
    def test_rectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(0,0),0)
        self.assertEqual(rectangle.perimeter(1,2), 6)
        self.assertEqual(rectangle.perimeter(1.5, 1.5), 6)
        self.assertEqual(rectangle.perimeter(123456789,987654321),2222222220)
        self.assertEqual(rectangle.perimeter(-18,18),"ONLY POSITIVE NUMBERS OR ALL ARE ZERO")
        self.assertEqual(rectangle.perimeter(0,1),"ONLY POSITIVE NUMBERS OR ALL ARE ZERO")
        self.assertEqual(rectangle.perimeter(True, 9),"WRONG ARGUMENT TYPE")
        self.assertEqual(rectangle.perimeter("999", 9),"WRONG ARGUMENT TYPE")