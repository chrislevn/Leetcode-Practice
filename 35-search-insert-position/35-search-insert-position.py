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
        
        n = len(nums)
    
        if nums[-1] < target : 
            return n
        if nums[-1] == target: 
            return n-1
        if nums[0] > target: 
            return 0
        if nums[0] == target: 
            return 0
        
        
        for i in range(n-1): 
            if nums[i] == target: 
                return i
            elif nums[i] < target and nums[i+1] > target: 
                return i + 1
            
       
            
        