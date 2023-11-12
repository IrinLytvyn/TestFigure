import math
import sys


class Figure:

    def perimeter(self):
        pass

    def area(self):
        pass

    def result(self):
        pass

    @staticmethod
    def distance_between_points(first_point, second_point):
        distance = math.sqrt(
            math.pow(second_point[0] - first_point[0], 2) + math.pow(second_point[1] - first_point[1], 2))
        return distance

    @staticmethod
    def cover_to_lst(point):
        result = list(map(int, point.split(',')))
        return result

    def return_result(self):
        return f'perimeter {self.perimeter()}, area {self.area()}'


class Square(Figure):

    def __init__(self, top_right=None, side=None):

        if top_right is not None:
            self.top_right = top_right
        else:
            self.top_right = input('Enter the Top Right (x,y): ')

        if side is not None:
            self.side = side
        else:
            try:
                self.side = int(input('enter the side: '))
            except ValueError:
                print('Side is a mandatory value')
                sys.exit()

    def result(self):
        if self.side <= 0:
            return 'Enter a positive side value'
        else:
            return self.return_result()

    def perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def area(self):
        area = math.pow(self.side, 2)
        return area


class Rectangle(Figure):

    def __init__(self, top_right_point=None, bottom_left_point=None):

        if top_right_point is not None:
            self.top_right_point = top_right_point
        else:
            top_right_point = input('enter the Top Right (x,y): ')
            try:
                self.top_right_point = self.cover_to_lst(top_right_point)
            except ValueError:
                print('Only numbers')
                sys.exit()

        if bottom_left_point is not None:
            self.bottom_left_point = bottom_left_point
        else:
            bottom_left_point = input('enter the Bottom Left (x,y): ')
            try:
                self.bottom_left_point = self.cover_to_lst(bottom_left_point)
            except ValueError:
                print('Only numbers')
                sys.exit()

        self.bottom_right_point = [self.top_right_point[0], self.bottom_left_point[1]]

        self.width = self.distance_between_points(self.bottom_right_point, self.bottom_left_point)
        self.height = self.distance_between_points(self.top_right_point, self.bottom_right_point)

    def result(self):
        if self.top_right_point[0] == self.bottom_left_point[0] or self.top_right_point[1] == self.bottom_left_point[1]:
            return "The figure isn't a rectangle"

        else:
            return self.return_result()

    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def area(self):
        area = self.width * self.height
        return area


class Circle(Figure):

    def __init__(self, center=None, radius=None):

        if center is not None:
            self.center = center
        else:
            self.center = input('enter the center (x,y): ')

        if radius is not None:
            self.radius = radius
        else:
            try:
                self.radius = int(input('enter the radius: '))
            except ValueError:
                print('Only numbers expected')
                sys.exit()

    def result(self):
        if self.radius <= 0:
            return 'Enter a positive radius value'
        else:
            return self.return_result()

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def area(self):
        area = math.pi * math.pow(self.radius, 2)
        return area


if __name__ == '__main__':

    figure = (input('enter the figure (square, rectangle or circle): ')).lower()

    if figure in ['square', 'rectangle', 'circle']:

        if figure == 'square':

            figure_class = Square()

        elif figure == 'rectangle':

            figure_class = Rectangle()

        elif figure == 'circle':

            figure_class = Circle()

        print(figure_class.result())

    else:
        print('You entered an incorrect figure name')
