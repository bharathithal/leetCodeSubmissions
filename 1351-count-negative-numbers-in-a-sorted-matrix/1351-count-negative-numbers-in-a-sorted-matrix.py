class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rr, cr = len(grid) - 1, len(grid[0]) - 1
        rl, cl = 0, 0
        res = 0
        
        if grid[rr][cr] >= 0:
            return 0
        
        while rl < rr:
            m = (rl + (rr - rl) // 2)
            if grid[m][cr] >= 0:
                rl = m + 1
            else:
                rr = m
        
        for i in range(rr, len(grid)):
            cl, cr = 0, len(grid[0]) - 1
            while cl < cr:
                m = cl + (cr - cl) // 2
                if grid[i][m] >= 0:
                    cl = m + 1
                else:
                    cr = m
            res += (len(grid[0]) - cr)
        
        return res
        