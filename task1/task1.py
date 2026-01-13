import sys

def path_circle(n, m):

    current = 1
    path = []

    while True:

        path.append(str(current))
        current = (current + m - 1) % n

        if current == 0:
            current = n

        if current == 1:
            break

    return ''.join(path)

def main():

    n1, m1, n2, m2 = map(int, sys.argv[1:5])

    path1 = path_circle(n1, m1)
    path2 = path_circle(n2, m2)

    result = path1 + path2
    print(result)

if __name__ == "__main__":
    main()