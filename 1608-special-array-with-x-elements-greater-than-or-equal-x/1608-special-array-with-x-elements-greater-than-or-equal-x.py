class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid       
        return -1 if left < n and left == nums[left] else left

        