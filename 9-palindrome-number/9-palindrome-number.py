class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        nums = []
        
        while x:
            nums.append(x % 10)
            x = x // 10
        
        l , r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
            
        return True
        