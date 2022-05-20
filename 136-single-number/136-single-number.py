class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for num in nums:
            if num not in l:
                l.append(num)
            else:
                l.remove(num)
        
        return l[0]
        