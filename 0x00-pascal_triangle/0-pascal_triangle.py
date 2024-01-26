#!/usr/bin/python3


def pascal_triangle(n):
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
