def permutations(array: list, begin: int, end: int):
    if begin >= end:
        print(array)
        return

    for i in range(begin, len(array)):
        if not check_duplication(array, begin, i):
            array[begin], array[i] = array[i], array[begin]
            permutations(array, begin + 1, end)  # notice
            array[begin], array[i] = array[i], array[begin]


def check_duplication(array: list, begin: int, cur_index: int) -> bool:
    for i in range(begin, cur_index):
        if array[i] == array[cur_index]:
            return True
    return False


if __name__ == "__main__":
    test_array = ["a", "b", "b"]
    permutations(test_array, 0, len(test_array))




