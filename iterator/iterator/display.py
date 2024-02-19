"""Print values and lists of values."""

from typing import List


def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    # For instance, if argument is False then return "No"
    if argument is False:
        return "No"
    # For instance, if argument is True then return "Yes"
    return "Yes"


def display_list(values: list, indent=""):
    """Display the provided list when iterating and printing every indented value."""
    # Iterate through all of the values inside of the list,
    # displaying them in the following fashion as shown in the README.md for this project
    for index, value in enumerate(values):
        print(f"{indent}2**{index} = {value}")
