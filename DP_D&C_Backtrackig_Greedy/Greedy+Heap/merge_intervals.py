a =  [[1,3],[2,4],[5,7],[6,8]]
aux = [a[0]]

i = 1

while i < len(a):
    if aux[-1][1] >= a[i][0]:
        #print("1")
        merged = [aux[-1][0], a[i][1]]
        print(merged)
        aux.append([aux[len(aux) - 1][0], a[i][1]])
        aux.pop(0)
    else:
        aux.append(a[i])
    i += 1

print(aux)

'''def main(a):



print(main([[1,9],[4,10],[3,11],[2,12]]))'''