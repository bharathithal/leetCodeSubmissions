class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1, st2 = [], []
        for char in s:
            if char != '#':
                st1.append(char)
            else:
                if len(st1) != 0:
                    st1.pop()
        
        for char in t:
            if char != '#':
                st2.append(char)
            else:
                if len(st2) != 0:
                    st2.pop()
            
        if st1 == st2:
            return True
        else:
            return False
            
        