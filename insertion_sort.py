def insertion_sort(a):
    """ sort an array using insertion sort """
    # split the sorted and unsorted, insert the unsorted into sorted.
    # a[0] is sorted and a[1:] is unsorted
    for j in range(1, len(a)):
        # save a[j], since we may overwrite it when shift right.
        temp = a[j]
        i = j - 1
        # a[0:j-1] is sorted, scan from right to left.
        while i >= 0 and a[i] > temp:
            # shift right, use i to track the insertion point.
            a[i + 1] = a[i]
            i -= 1
        # be careful with this edge case.
        # if a[j] > all nodes to its left, the above is not executed. a[j] stay same.
        # if we found a node is greater than a[j], we make a seat for a[j]
        a[i + 1] = temp

    return a


if __name__ == '__main__':
    print(insertion_sort([4, 1, 3, 8, 4, 5]))

    import random

    n = 20
    a = list(range(n))
    random.shuffle(a)
    print(a)
    assert (insertion_sort(a) == list(range(n)))
