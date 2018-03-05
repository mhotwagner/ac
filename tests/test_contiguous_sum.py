from contiguous_sum import max_contiguous_sum, max_contiguous_sub_array


def test_max_contiguous_sum() -> None:
    assert max_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7


def test_max_contiguous_sub_array() -> None:
    assert max_contiguous_sub_array([-2, -3, 4, -1, -2, 1, 5, -3]) == [4, -1, -2, 1, 5]


def test_weird_max_contiguous_sub_array() -> None:
    assert max_contiguous_sub_array([10, -1, -1]) == [10]
