class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        
        for index in nums1:
            if index not in dictionary:
                dictionary[index] = 1
                
        for index in nums2:
            if index in dictionary and dictionary[index] != 2:
                dictionary[index] += 1
        
        newList = []
        for key, value in dictionary.items():
            if value == 2:
                newList.append(key)
                
        return newList
        