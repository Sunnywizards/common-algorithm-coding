'''
Radix sort (ascending order)
The first one is to use the sort function with lambda in Python to implement the basket sort process,
and the second one is what I implemented it by manual
'''

import copy

def radix_sort(array: list):
    max_digit_num = get_max_digit_num(array)
    tmp_array = copy.deepcopy(array)
    for i in range(1, max_digit_num + 1):
        tmp_array.sort(key = lambda x: x % (10 ** i) // (10 ** (i - 1)), reverse = False)
    return tmp_array

def radix_sort_manual(array: list):
    max_digit_num = get_max_digit_num(array)
    tmp_array = copy.deepcopy(array)
    basket = [[] for _ in range(10)]
    for i in range(1, max_digit_num + 1):
        for num in tmp_array:
            n = int(num % (10 ** i) // (10 ** (i - 1)))
            basket[n].append(num)
        tmp_array.clear()
        for bas in basket:
            for element in bas:
                tmp_array.append(element)
            bas.clear()
    return tmp_array

def get_max_digit_num(array: list) -> int:
    if len(array) < 1:
        return 0
    max_digit_num = 1
    for num in array:
        while int(num/(10**(max_digit_num))) > 0:
            max_digit_num += 1
    return max_digit_num

if __name__ == "__main__":
    test_array = [1, 10268, 25, 360, 125, 30, 7, 2048, 12]
    print(radix_sort_manual(test_array))
    print(radix_sort(test_array))