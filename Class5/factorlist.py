def factors(n):
    """
This function consumes a positive integer, n
This function produces a list of positive integers which divide n (in ascending order)
    """
    factor_list = []
    for potential_factor in range(1, n+1):
        if (n % potential_factor == 0):
            factor_list.append(potential_factor)
    return factor_list

assert factors(1) == [1]
assert factors(4) == [1, 2, 4]
assert factors(7) == [1, 7]
assert factors(10) == [1, 2, 5, 10]

print("All tests passed!")