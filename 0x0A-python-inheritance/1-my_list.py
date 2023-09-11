#!/usr/bin/python3
"""MyList class """


class MyList(list):
    """ A subclass of lidy."""
    def print_sorted(self):
        """Print the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)

        def __str__(self):
            """Override the string representation to match the sorted list."""
            return str(sorted(self))
