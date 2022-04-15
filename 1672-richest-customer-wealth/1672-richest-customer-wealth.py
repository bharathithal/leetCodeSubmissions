class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        for account in accounts:
            total = 0
            for num in account:
                total += num
                sum = max(total, sum)
                
        return sum
        