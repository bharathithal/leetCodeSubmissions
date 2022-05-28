class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[-1]):
            if i != nums[i]:
                return i
        
        return nums[-1] + 1
        