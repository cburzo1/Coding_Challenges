# can sort two arrays that are already sorted
def main(a, start, mid, end):
    print(a[start],a[int(mid) - 1], a[int(mid)], a[end])

    a1 = []
    a2 = []

    for i in range(start, int(mid)):
        a1.append(a[i])

    for i in range(int(mid), end + 1):
        a2.append(a[i])

    i = 0
    j = 0
    a3 = []

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a3.append(a1[i])
            i += 1
        else:
            a3.append(a2[j])
            j += 1

    while i < len(a1):
        a3.append(a1[i])
        i += 1

    while j < len(a2):
        a3.append(a2[j])
        j += 1

    print(a3)

print(main([1, 6, 8, 2, 5, 19, 22], 0, (0 + 7)/2, 6))

