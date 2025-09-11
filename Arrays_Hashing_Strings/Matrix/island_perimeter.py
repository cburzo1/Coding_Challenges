def main(mx):
    i, j = 0, 0

    if j - 1 >= 0:
        left = mx[i][j - 1]
    else:
        left = None

    if j + 1 <= 0:
        right = mx[i][j + 1]
    else:
        right = None

    print(left, right)
    #for i in range(0, len(mx)):
        #for j in range(0, len(mx[i])):
            #print(mx[i][j], end = " ")

        #print()

print(main([
  [1, 1],
  [1, 1]
]))