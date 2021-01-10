'''
Shell sort
'''

def shell_sort(array: list):
    len_array = len(array)
    gap = len_array // 2
    while gap >= 1:
        for i in range(gap, len_array):
            for j in range(i - gap, -1, -gap):
                if array[j] > array[j + gap]:
                    array[j], array[j + gap] = array[j + gap], array[j]
        gap = gap // 2

if __name__ == "__main__":
    test_array = [100, 10268, 25, 360, 125, 30, 7, 2048, 12]
    shell_sort(test_array)
    print(test_array) # [7, 12, 25, 30, 100, 125, 360, 2048, 10268]