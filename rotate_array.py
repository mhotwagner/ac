
# assert rotate_array([1, 2, 3], 1) == [3, 1, 2]
# assert rotate_array([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]


def rotate_array(original_list: list, n: int=0) -> list:
    print(original_list[-1*n:])
    print(original_list[:-1*n])
    return original_list[-1*n:] + original_list[:-1*n]
