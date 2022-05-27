class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num > 0:
            if num % 2:
                num -= 1
                res += 1
            else:
                num = num // 2
                res += 1
        
        return res
                