from rotate_array import rotate_array


def test_rotate_array_returns_a_list() -> None:
    assert type(rotate_array([1, 3, 3])) == list


def test_rotate_array_rotates_the_list_to_the_right_for_a_positive_integer() -> None:
    assert rotate_array([1, 2, 3], 1) == [3, 1, 2]


def test_rotate_array_still_works() -> None:
    assert rotate_array([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]

