#Brute Force
def main(a):
    aux = []

    for i in range(0, len(a)):
        prod = 1
        for j in range(0, len(a)):
            if j != i:
                prod *= a[j]

        aux.append(prod)

    print(aux)

print(main([1,2,3,4]))