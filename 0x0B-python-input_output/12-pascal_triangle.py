#!/usr/bin/python3
"""A function representing Pascal's triangle of n."""


def pascal_triangle(n):
    """Initialize the pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

    for j in range(1, i):
        prev_row = triangle[i - 1]
        new_value = prev_row[j - 1] + prev_row[j]
        row.append(new_value)

        row.append(1)
        triangle.append(row)
    return triangle
