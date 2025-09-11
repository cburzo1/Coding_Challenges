#MY IMPL
'''def main(mx):

    count = 0

    for i in range(0, len(mx)):
        for j in range(0, len(mx[i])):
            left = 0
            right = 0
            up = 0
            down = 0
            if mx[i][j] == 1:

                if j - 1 < 0:
                    left = None

                if j + 1 > len(mx[i]) - 1:
                    right = None

                if i - 1 < 0:
                    up = None

                if i + 1 > len(mx) - 1:
                    down = None

                if left is None or mx[i][j - 1] == 0:
                    count += 1

                if right is None or mx[i][j + 1] == 0:
                    count += 1

                if up is None or mx[i - 1][j] == 0:
                    count += 1

                if down is None or mx[i + 1][j] == 0:
                    count += 1

    print(count)'''

# REFINED
def main(mx):
    count = 0
    rows, cols = len(mx), len(mx[0])

    for i in range(rows):
        for j in range(cols):
            if mx[i][j] == 1:
                # left
                if j - 1 < 0 or mx[i][j - 1] == 0:
                    count += 1
                # right
                if j + 1 >= cols or mx[i][j + 1] == 0:
                    count += 1
                # up
                if i - 1 < 0 or mx[i - 1][j] == 0:
                    count += 1
                # down
                if i + 1 >= rows or mx[i + 1][j] == 0:
                    count += 1

    #print(count)
    return count

print(main([
  [0,1, 0, 0],
  [0,1, 1, 0],
  [0,1, 1, 0]
]))