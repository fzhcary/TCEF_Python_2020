# Selection Sort
def selection_sort(nums):
    size = len(nums)

    for j in range(1, size):
        # on the last run, j: size -1
        max_number = nums[size - j]
        max_i = size - j
        for i in range(0, size - j):
            if nums[i] > max_number:
                max_i = i
                max_number = nums[i]

        # swap max_i and size-1
        nums[max_i], nums[size - j] = nums[size - j], nums[max_i]

    return nums


if __name__ == "__main__":
    import random

    print(selection_sort([]))
    print(selection_sort([1]))
    print(selection_sort([26, 54, 93, 17, 77, 31, 44, 55, 20]))

    n = 20
    a = list(range(n))
    random.shuffle(a)
    print(a)
    assert(selection_sort(a) == list(range(n)))



