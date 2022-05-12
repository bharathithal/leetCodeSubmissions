class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        
        i = 0
        for char in s:
            if d[char] == 1:
                return i
            i += 1
        
        return -1