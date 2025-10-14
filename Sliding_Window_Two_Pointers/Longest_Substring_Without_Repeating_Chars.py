# brute force time limit exceeded
def main(s):
    s_l = list(s)
    biggest = 0
    aux = []

    for i in range(0, len(s_l)):
        count = 0

        for j in range(i, len(s_l)):
            #print(s_l[j])
            if s_l[j] in aux:
                print("if: ", s_l[j])
                if count > biggest:
                    biggest = count
                aux = []
                break
            else:
                print("else: ", s_l[j])
                aux.append(s_l[j])
                count += 1
                if count > biggest:
                    biggest = count

    return biggest

def main2(s):


#print(main("abcbcbb"))
print(main("c"))