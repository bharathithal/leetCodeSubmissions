class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        m, l, r = 0, 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        if nums[m] > target:
            return m
        
        else:
            return m+1
        