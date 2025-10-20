#O(n^2) brute force
def main(s1, s2):

    s1_l = list(s1)
    s2_l = list(s2)

    if len(s2_l) != len(s1_l):
        return False

    for i in range(0, len(s1_l)):
        for j in range (0, len(s2_l)):
            if s1_l[i] == s2_l[j]:
                s2_l.pop(j)
                break

    print(s1_l, s2_l)

    if len(s2_l) == 0:
        return True
    else:
        return False

#O(n) optimized
def main_op(s1, s2):
    s1_l = list(s1)
    s2_l = list(s2)

    dict_s1 = {}
    dict_s2 = {}

    if len(s2_l) != len(s1_l):
        return False

    for i in range(0, len(s1_l)):
        if s1_l[i] not in dict_s1:
            dict_s1[s1_l[i]] = 1
        else:
            dict_s1.update({s1_l[i]:dict_s1.get(s1_l[i]) + 1})

    for i in range(0, len(s2_l)):
        if s2_l[i] not in dict_s2:
            dict_s2[s2_l[i]] = 1
        else:
            dict_s2.update({s2_l[i]: dict_s2.get(s2_l[i]) + 1})

    print(dict_s1 == dict_s2)

    return dict_s1 == dict_s2

print(main_op("ctat", "tctt"))