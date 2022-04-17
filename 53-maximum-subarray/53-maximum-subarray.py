class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            res = max(res, currSum)
            
        return res
            
        