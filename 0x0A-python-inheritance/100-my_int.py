#!/usr/bin/python3
"""Define a class MyInt, inherited from int."""


class MyInt(int):
    """Invert int operators == and !=."""
    def __eq__(self, other):
        """Overide == with !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overide != with ==."""
        return super().__eq__(other)
