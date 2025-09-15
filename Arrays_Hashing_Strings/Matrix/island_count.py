def main(mx):
    Q = []
    count = 0

    for i in range(0, len(mx)):
        for j in range(0, len(mx[i])):
            if mx[i][j] == "1":
                Q.append([i, j])

    print(Q)
    removed_item = Q.pop(0)
    count += 1

    #while len(Q) > 0:
    if [removed_item[1], removed_item[1] - 1] in Q:
        removed_item = Q.pop(Q.index([removed_item[1], removed_item[1] - 1]))

    elif [removed_item[1] - 1, removed_item[1]] in Q:
        removed_item = Q.pop(Q.index([removed_item[1] - 1, removed_item[1]]))

    elif [removed_item[1], removed_item[1] + 1] in Q:
        removed_item = Q.pop(Q.index([removed_item[1], removed_item[1] + 1]))

    elif [removed_item[1] + 1, removed_item[1]] in Q:
        removed_item = Q.pop(Q.index([removed_item[1] + 1, removed_item[1]]))
    else:
        removed_item = Q.pop(0)
        count += 1

    print(removed_item, Q)

print(main([
  ["1","1","0","0","1"],
  ["1","1","0","0","1"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

'''print(main([
  ["1","0","0","0"],
  ["0","0","0","0"],
  ["0","0","0","0"],
  ["0","0","0","0"]
]))

print(main([
  ["1","0","1","0"],
  ["0","1","0","1"],
  ["1","0","1","0"],
  ["0","1","0","1"]
]))'''