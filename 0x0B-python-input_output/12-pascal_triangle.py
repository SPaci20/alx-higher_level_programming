#!/usr/bin/python3
"""A function representing Pascal's triangle of n."""


def pascal_triangle(n):
    """Initialize the pascal's triangle."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        triangle.append(row)

    return triangle
