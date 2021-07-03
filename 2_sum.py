def twoSum(nums, target):
    dct = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in dct:
            return [i, nums.index(diff)]
        else:
            dct[diff] = 0
print(twoSum([2,3,7,9],5))