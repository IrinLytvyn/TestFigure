import unittest
from main import square, rectangle, circle


class TestSquare(unittest.TestCase):

    def test_square(self):
        result = square(1)
        self.assertEqual(result, 'perimeter 4, area 1.0')

    def test_square_negative(self):
        result = square(-1)
        self.assertEqual(result, 'Enter a positive side value')


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        result = rectangle([0, 0], [1, 2])
        self.assertEqual(result, 'perimeter 6.0, area 2.0')

    def test_rectangle_fail(self):
        result = rectangle([1, 1], [1, 0])
        self.assertEqual(result, "The figure isn't a rectangle")


class TestCircle(unittest.TestCase):

    def test_circle(self):
        result = circle(2)
        self.assertEqual(result, 'perimeter 12.566370614359172, area 12.566370614359172')

    def test_circle_fail(self):
        result = circle(0)
        self.assertEqual(result, 'Enter a positive radius value')
