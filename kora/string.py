""" String processing utilities
"""

def ranges_to_list(range_str):
    """ ranges_to_list("1-3,5-7") == [1,2,3,5,6,7] """
    num_list = []
    for rng in range_str.split(','):
        a, b = map(int, rng.split('-'))
        num_list.extend(range(a, b+1))
    return num_list
