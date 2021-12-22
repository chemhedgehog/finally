def min_max_pairs(nums):
    nums=sorted(nums)
    sums=[]
    for i in range(int(len(nums)/2)):
        sums.append(nums[i]+nums[len(nums)-i-1])
    return max(sums)

print(min_max_pairs([3,5,4,2,4,6]))