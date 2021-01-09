'''
Non recursive way to implement quick sort
Compared with recursive way, this method utilizes the while loop to replace invoking the function itself
In quick sort, should notice the relation among left, partition_index and right
'''
import logging

def partition(array:list, left:int, right:int):
    if left >= right:
        logging.exception("Illegal Input")
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
    return left_pointer

def quick_sort(array: list):
    if len(array) < 2:
        return
    left = 0
    right = len(array) - 1
    stack = list()
    stack.append(right)
    stack.append(left)
    while len(stack) > 0:
        left = stack.pop()
        right = stack.pop()
        if left < right:
            partition_index = partition(array, left, right)
            if partition_index < right:
                stack.append(right)
                stack.append(partition_index + 1)
            if partition_index > left:
                stack.append(partition_index - 1)
                stack.append(left)

if __name__ == "__main__":
    test_array = [3, 6, 5, 9, 1, 7, -1, 3]
    quick_sort(test_array)
    print(test_array) # [-1, 1, 3, 3, 5, 6, 7, 9]





