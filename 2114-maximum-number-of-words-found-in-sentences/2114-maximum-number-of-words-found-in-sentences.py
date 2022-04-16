class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            arr = sentence.split(" ")
            length = len(arr)
            res = max(res, length)
        
        return res