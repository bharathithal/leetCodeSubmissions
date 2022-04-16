class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        res = [False] * len(candies)
        i = 0
        
        for num in candies:
            if(num+extraCandies >= highest):
                res[i] = True
            i += 1
                
        return res        