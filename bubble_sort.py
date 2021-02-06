def bubble_sort(nums):
    while True:
        swapped = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swapped = True

        if not swapped:
            break

    return nums
