class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        arr = []
        for operation in operations:
            if(operation == "--X" or operation == "X--"):
                arr.append(-1)
                
            if(operation == "++X" or operation == "X++"):
                arr.append(1)
                
        res = sum(arr)
        return res
                
            