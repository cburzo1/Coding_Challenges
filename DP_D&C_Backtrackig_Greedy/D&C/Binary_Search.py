# My attempt
# Binary searches must be sorted. The sort function is a timsort (mixture of insertion and merge sort)
def main(a, start, end, key):

    if start > end:
        return "not found"

    mid = int((start + end)/2)

    if key == a[mid]:
        return "found: " + str(mid)
    elif key < a[mid]:
        return main(a, start, mid - 1, key)
    else:
        return main(a, mid + 1, end, key)

print(main([3, 6,9,10, 23, 24, 30, 31], 0, 7, 31))