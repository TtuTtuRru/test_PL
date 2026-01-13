import sys

def read_ellipse(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()
        cx, cy = map(float, lines[0].strip().split())
        rx, ry = map(float, lines[1].strip().split())

    return cx, cy, rx, ry

def read_points(file_path):

    points = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                x, y = map(float, line.strip().split())
                points.append((x, y))
    return points

def check_point(rx, ry, x, y):

    result = (x ** 2 / rx ** 2) + (y ** 2 / ry ** 2)

    if result == 1:
        return 0
    elif result < 1:
        return 1
    else:
        return 2

def main():

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    cx, cy, rx, ry = read_ellipse(ellipse_file)
    points = read_points(points_file)

    for x, y in points:
        if cx != 0:
            x = x - cx
        if cy != 0:
            y = y - cy
        position = check_point(rx, ry, x, y)
        print(position)

if __name__ == "__main__":
    main()