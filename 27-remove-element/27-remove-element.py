class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        for i in range(length-1, -1, -1): 
            if nums[i] == val: 
                del nums[i]
                length -= 1
        return length