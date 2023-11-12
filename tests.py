import unittest
# from main import square, rectangle, circle
from main2 import Square, Rectangle, Circle


class TestSquare(unittest.TestCase):

    def test_square(self):
        square = Square([1, 1], 1)
        result = square.result()
        self.assertEqual(result, 'perimeter 4, area 1.0')

    def test_square_negative(self):
        square = Square([1, 1], -1)
        result = square.result()
        self.assertEqual(result, 'Enter a positive side value')


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        rectangle = Rectangle([0, 0], [1, 2])
        result = rectangle.result()
        self.assertEqual(result, 'perimeter 6.0, area 2.0')

    def test_rectangle_fail(self):
        rectangle = Rectangle([1, 1], [1, 0])
        result = rectangle.result()
        self.assertEqual(result, "The figure isn't a rectangle")


class TestCircle(unittest.TestCase):

    def test_circle(self):
        circle = Circle([1, 1], 2)
        result = circle.result()
        self.assertEqual(result, 'perimeter 12.566370614359172, area 12.566370614359172')

    def test_circle_fail(self):
        circle = Circle([1, 1], 0)
        result = circle.result()
        self.assertEqual(result, 'Enter a positive radius value')
