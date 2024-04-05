#!/usr/bin/python3
"""Function that returns a pascal triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    1. Returns an empty list if n <= 0
    2. You can assume n will be always an integer
    """
    triangles = []

    for a in range(n):
        if len(triangles) == 0:
            triangles.append([1])
            continue
        prev = triangles[-1]
        new_arr = [1]
        for b in range(1, a):
            x = prev[b - 1]
            y = prev[b]
            new_arr.append(x+y)
        new_arr.append(1)
        triangles.append(new_arr)

    return triangles


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(3))
