class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        first, last = 0, len(nums)-1
        while first <= last:
            mid = first + (last-first // 2)
            
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                return mid
            
        return -1
            