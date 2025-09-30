def main(a):

    aux = []
    aux_2 = []

    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i != j:
                for k in range(0, len(a)):
                    if j != k and k != i:
                        if a[i] + a[j] + a[k] == 0:
                            aux.append([a[i], a[j] ,a[k]])

    

    for i in range(0, len(aux)):


print(main([-1,0,1,2,-1,-4]))