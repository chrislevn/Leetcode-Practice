class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        """
        nums = [1,3,5,6], target = 2
        nums = [1,2,3,5,6]
        1
        
        nums = [1,3,5,6], target = 7
        nums = [1,3,5,6,7]
        -> 4
        
        nums = [1,3,5,6], target = 4
        [1,3,4,5,6]
        return pivot[index of 3] + 1
        
        Input: nums = [1,3,5,6], target = 7

        
        """
        
        nums.append(target)
        nums = sorted(nums)
        
        return nums.index(target)
            
        