#!/usr/bin/python3
"""Define  a class Student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Represent student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance."""
        serialized_student = {}
        for attr_name in dir(self):
            if not attr_name.startswith('_'):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (str, int)):
                    serialized_student[attr_name] = attr_value
        return serialized_student
