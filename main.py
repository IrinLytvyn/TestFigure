import math


def distance_between_points(first_point, second_point):
    distance = math.sqrt(math.pow(second_point[0] - first_point[0], 2) + math.pow(second_point[1] - first_point[1], 2))
    return distance


def cover_to_lst(point):
    result = list(map(int, point.split(',')))
    return result


def square(side):
    if side <= 0:
        return 'Enter a positive side value'

    else:
        perimeter = 4 * side
        area = math.pow(side, 2)
        return f'perimeter {perimeter}, area {area}'


def rectangle(top_right_point, bottom_left_point):
    if top_right_point[0] == bottom_left_point[0] or top_right_point[1] == bottom_left_point[1]:
        return "The figure isn't a rectangle"

    else:
        bottom_right_point = [top_right_point[0], bottom_left_point[1]]

        width = distance_between_points(bottom_right_point, bottom_left_point)
        height = distance_between_points(top_right_point, bottom_right_point)

        perimeter = 2 * (width + height)
        area = width * height

        return f'perimeter {perimeter}, area {area}'


def circle(radius):
    if radius <= 0:
        return 'Enter a positive radius value'

    else:
        perimeter = 2 * math.pi * radius
        area = math.pi * math.pow(radius, 2)
        return f'perimeter {perimeter}, area {area}'


if __name__ == '__main__':

    figure = (input('enter the figure (square, rectangle or circle): ')).lower()

    if figure == 'square':

        top_right = input('Enter the Top Right (x,y): ')

        try:
            side = int(input('enter the side: '))
            print(square(side))
        except ValueError:
            print('Only numbers expected')

    elif figure == 'rectangle':

        top_right = input('enter the Top Right (x,y): ')
        bottom_left = input('enter the Bottom Left (x,y): ')

        try:
            top_right_point = cover_to_lst(top_right)
            bottom_left_point = cover_to_lst(bottom_left)

            print(rectangle(top_right_point, bottom_left_point))

        except ValueError:
            print('Only numbers expected')

    elif figure == 'circle':

        center = input('enter the center (x,y): ')

        try:
            radius = int(input('enter the radius: '))
            print(circle(radius))
        except ValueError:
            print('Only numbers expected')

    else:
        print('You entered an incorrect figure name')
