#brute force all positives
def main(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1

    return count

def main2(nums, k):
    prefix_sum = 0
    count = 0
    prefix_counts = {0: 1}  # base case: sum 0 occurs once

    for num in nums:
        prefix_sum += num

        # check if (current_sum - k) has been seen
        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum - k]

        # record current prefix_sum
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    return count

print(main([1,1,1], 2))
print(main([1,2,3], 3))