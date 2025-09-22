#Brute Force
def main(a, t):

    for i in range(0, len(a)):
        for j in range(1, len(a)):
            if a[i] + a[j] == t:
                return [i, j]

# My Optimal attempt
def main_o(a, t):

    dict_a = {}

    for i in range(0, len(a)):
        if i not in dict_a:
            dict_a[a[i]] = i

    #print(dict_a)

    keys = dict_a.keys()

    for key in keys:
        if t - key in dict_a:
            print(dict_a[key])

#correct optimal
def two_sum(nums, target):
    dict_a = {}  # value → index

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dict_a:
            return [dict_a[complement], i]
        dict_a[num] = i

print(two_sum([2,7,11,15, 3, 6], 5))