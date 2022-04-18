class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for jewel in jewels:
            for stone in stones:
                if stone==jewel:
                    res += 1
        return res
        