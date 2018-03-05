

# max_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3]) -> 7


def max_contiguous_sum(numbers: list) -> int:
    highest = numbers[0]
    local_highest = highest

    for index, x in enumerate(numbers[1:]):
        local_highest += x
        if x > local_highest:
            local_highest = x
        if local_highest > highest:
            highest = local_highest

    return highest


def max_contiguous_sub_array(numbers: list) -> list:
    i, f = 0, 1
    highest = numbers[0]
    local_highest = highest

    for index, x in enumerate(numbers[1:]):
        index += 1
        local_highest += x
        if x > local_highest:
            local_highest = x
            i = index
        if local_highest > highest:
            highest = local_highest
            f = index + 1

    return numbers[i:f]
