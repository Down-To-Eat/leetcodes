
class Solution:
    def twoSum(self, nums, target):
        o = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i] + nums[j]

                if x == target:
                    o.append(i)
                    o.append(j)
                    return o
nums = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))