class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = []
        currMin = nums[0]
        
        for num in nums[1:]:
            while l and num >= l[-1][0]:
                l.pop()
            if l and num > l[-1][1]:
                return True
            
            l.append([num, currMin])
            currMin = min(num, currMin)
        
        return False
                