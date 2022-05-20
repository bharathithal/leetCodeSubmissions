class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        p = 0
        while p < len(nums)-2:
            if nums[p] != nums[p+1]:
                return nums[p]
            p += 2
        
        return nums[-1]
        