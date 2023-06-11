#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extend the tuples to have at least 2 elements
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Perform the addition of the elements
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    # Return the resulting tuple
    return (sum_1, sum_2)
