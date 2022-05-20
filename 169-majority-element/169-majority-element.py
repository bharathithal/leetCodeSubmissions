class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        n = len(nums) / 2
        
        for num, freq in d.items():
            if freq > n:
                return num
            
        