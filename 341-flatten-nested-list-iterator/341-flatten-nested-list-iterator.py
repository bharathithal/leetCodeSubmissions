# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.flattenList(nestedList)
        
    def flattenList(self, nestedList):
        for item in nestedList:
            if(not item.isInteger()):
                self.flattenList(item.getList())
            else:
                self.queue.append(item.getInteger())
                
    def next(self) -> int:
        return self.queue.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.queue) > 0
