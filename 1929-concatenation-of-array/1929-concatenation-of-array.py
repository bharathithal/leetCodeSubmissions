class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        results = []
        
        for i in range(len(nums)):
            results.append(nums[i])

        for i in range(len(nums)):
            results.append(nums[i])
        
        return results