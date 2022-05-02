class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = set()
        for num in nums1:
            if num not in h:
                h.add(num)
        res = []       
        for num in nums2:
            if num in h and num not in res:
                res.append(num)
        
        return res
        