class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)): 
            result.append(nums2.index(nums1[i]))
        return result
        