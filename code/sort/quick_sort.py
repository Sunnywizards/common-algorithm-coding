'''
Recursive way to implement quick sort
'''

def quick_sort(array:list, left:int, right:int):
    if left >= right:
        return
    pivot = array[left]
    left_pointer = left
    right_pointer = right
    while left_pointer < right_pointer:
        while array[right_pointer] >= pivot and left_pointer < right_pointer:
            right_pointer -= 1
        if left_pointer < right_pointer:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
        while array[left_pointer] <= pivot and left_pointer < right_pointer:
            left_pointer += 1
        if left_pointer < right_pointer:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
    quick_sort(array, left, left_pointer - 1)
    quick_sort(array, left_pointer + 1, right)

if __name__ == "__main__":
    test_array = [3, 6, 5, 9, 1, 7, -1, 3]
    quick_sort(test_array, 0, len(test_array) - 1)
    print(test_array) # [-1, 1, 3, 3, 5, 6, 7, 9]





