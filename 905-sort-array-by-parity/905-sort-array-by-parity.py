class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num % 2 == 0:
                res.append(num)

        for num in nums:
            if num % 2 != 0:
                res.append(num)

        return res