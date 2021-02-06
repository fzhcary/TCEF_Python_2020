def merge_sorted_list(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if not left:
        result.extend(right)
    else:
        result.extend(left)
    return result


def merge_sort(nums):
    size = len(nums)
    if size <= 1:
        return nums

    mid = size // 2
    left, right = nums[:mid], nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted_list(left, right)


if __name__ == "__main__":
    import random
    n = 1000
    a = list(range(n))
    random.shuffle(a)
    print(a)
    assert(merge_sort(a) == list(range(n)))
