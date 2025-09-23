import re

#explicit two pointers
def main(s):

    st = re.sub(r'[^a-zA-Z0-9]','', s).lower()

    st_l = list(st)

    i = 0
    j = len(st_l) - 1

    while i < j:
        temp = st_l[i]
        st_l[i] = st_l[j]
        st_l[j] = temp

        i += 1
        j -= 1

    st2 = "".join(st_l)

    if st2 == st:
        return "Valid Palindrome"
    else:
        return "InValid Palindrome"

#more Pythonic
def main2(s):
    st = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    st2 = st[::-1] #start from back and reverse

    if st2 == st:
        return "Valid Palindrome"
    else:
        return "InValid Palindrome"

print(main2("ra_$caeR"))