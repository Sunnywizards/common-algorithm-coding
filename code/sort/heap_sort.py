'''
Heap sort
'''

import copy

def heap_sort(wait_heap_array: list) -> list:
    array = copy.deepcopy(wait_heap_array)
    index = 0
    result = []
    while len(array) > 0:
        build_heap(array, index)
        top_element = array.pop(0)
        result.append(top_element)
        index += 1
    return result

def build_heap(array: list, index):
    len_array = len(array)
    for i in range((int(len_array/ 2) - 1), -1, -1):
        if array[i] > array[2 * i + 1]:
            array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
        if 2 * i + 2 < len_array:
            if array[i] > array[2 * i + 2]:
                array[i], array[2 * i + 2] = array[2 * i + 2], array[i]

if __name__ == "__main__":
    test_array = [3, 6, 5, 9, 1, 7, -1, 3, 8, 0]
    test_array = heap_sort(test_array)
    print(test_array) # [-1, 0, 1, 3, 3, 5, 6, 7, 8, 9]