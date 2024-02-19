"""Calculate the powers of two, with iteration, from minimum to maximum values."""


def calculate_powers_of_two_for_loop(minimum: int, maximum: int):
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    # Leveraging your notes, the course slides, and your notes,
    # please provide a complete implementation of this function that 
    # produces the correct output as shown in the README.md file.
    for c in range(minimum, maximum):
        ans = 2**c
        powers_list.append(ans)

    return powers_list


def calculate_powers_of_two_while_loop(minimum: int, maximum: int):
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    counter = minimum

    while counter < maximum:
        ans = 2**minimum
        counter += 1
        powers_list.append(ans)

    return powers_list
