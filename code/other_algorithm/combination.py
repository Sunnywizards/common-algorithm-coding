def combine(array: list, result_list: list, index: int):
    if index == len(array):
        if len(result_list) != 0:
            print(result_list)
        return

    result_list.append(array[index])

    combine(array, result_list, index + 1)
    result_list.pop(-1)
    combine(array, result_list, index + 1)


if __name__ == "__main__":
    arr = ['a', 'b', 'c']
    combine(arr, [], 0)