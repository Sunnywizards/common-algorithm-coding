'''
Merge sort
'''

def merge_sort(array: list, left: int, right: int):
    if left >= right:
        return
    center = int((left + right) / 2)
    merge_sort(array, left, center)
    merge_sort(array, center + 1, right)
    merge(array, left, center, center + 1, right)

def merge(array: list, left1: int, right1: int, left2: int, right2: int):
    if left1 <= right1 and left2 <= right2:
        tmp_array = []
        index = 0
        pointer1, pointer2 = left1, left2

        while pointer1 <= right1 and pointer2 <= right2:
            if array[pointer1] <= array[pointer2]:
                tmp_array.append(array[pointer1])
                pointer1 += 1
                index += 1
            else:
                tmp_array.append(array[pointer2])
                pointer2 += 1
                index += 1

        if pointer1 > right1:
            tmp_array[index:] = array[(pointer2): (right2 + 1)]
        else:
            tmp_array[index:] = array[(pointer1): (right1 + 1)]

        array[left1: (right2 + 1)] = tmp_array


if __name__ == "__main__":
    test_array = [3, 6, 5, 9, 1, 7, -1, 3, 8, 0]
    merge_sort(test_array, 0, len(test_array) - 1)
    print(test_array) # [-1, 0, 1, 3, 3, 5, 6, 7, 8, 9]