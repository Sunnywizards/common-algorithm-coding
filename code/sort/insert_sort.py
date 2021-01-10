'''
Insert sort
'''

def insert_sort(array: list):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

if __name__ == "__main__":
    test_array = [3, 6, 5, 9, 1, 7, -1, 3, 8, 0]
    insert_sort(test_array)
    print(test_array) # [-1, 0, 1, 3, 3, 5, 6, 7, 8, 9]
