class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (n * 2)
        for i in range(n*2):
            if(i%2 == 0):
                res[i] = nums[i//2]
            else:
                res[i] = nums[n + (i//2)]
                
        return res
            
        