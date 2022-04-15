class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = 0
        for num in nums:
            ans[i] = nums[num]
            i += 1
        
        return ans
        