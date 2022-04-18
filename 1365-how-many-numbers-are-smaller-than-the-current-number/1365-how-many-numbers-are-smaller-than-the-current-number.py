class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        res = []
        
        for num in nums:
            freq[num] += 1
        
        for i in range(1, 101):
            freq[i] += freq[i-1]
        
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(freq[num-1])
        
        return res
            