def main(a):
    largest_con = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            current_con = (j - i ) * min(a[i], a[j])
            if current_con > largest_con:
                #print(i, j, a[i], current_con)
                largest_con = current_con

    return largest_con

#do optimal

print(main([1,8,6,2,5,4,8,3,7]))
print(main([1,8,6,2]))