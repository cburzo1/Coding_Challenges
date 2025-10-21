def main(s1, t):
    t1 = t
    s1_l = list(s1)
    t_l = list(t)

    smallest = 20

    count = 0

    aux = []

    for i in range(0, len(s1_l)):
        for j in range(i, len(s1_l)):
            count += 1
            if s1_l[j] in t_l:
                t_l.pop(t_l.index(s1_l[j]))

            if len(t_l) == 0:
                if count < smallest:
                    smallest = count
                break

        t_l = list(t1)
        count = 0


    print(smallest, aux)

print(main("ADOBECODEBANC", "ABC"))