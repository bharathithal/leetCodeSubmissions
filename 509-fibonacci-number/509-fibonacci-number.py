class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        memo = [0, 1]
        for _ in range(2, n + 1):
            memo = [memo[-1], memo[-1] + memo[-2]]

        return memo[-1]
        
        