class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = right = 0
        res = len(nums) + 1
        while right < len(nums):
            total += nums[right]
            while total >= target:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return res if res <= len(nums) else 0
                