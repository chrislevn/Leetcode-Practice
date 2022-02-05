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
        
        
        nums = [1,3,5,6], target = 5
        mid = len(nums) / 2
    
        nums[mid] # 5 == 5 return mid
        
        
        nums = [1,2,3,5,6], target = 2
        mid = 2
        nums[mid] = 5 > 2
        0 - 2
        mid = 2 // 2 = 1
        3 > 2
        0 1 // 2= 0
        
        nums[0] = 1 < 2
        ret
        
        nums = [1,3,5,6], target = 2
        
        
        """

        
        left, right = 0, len(nums)-1
        
        if nums[0] == target: 
            return 0
        if nums[-1] < target: 
            return right + 1
        if nums[0] > target: 
            return 0
    
        while (right - left) > 1:
            mid = (left+right+1) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: 
                left = mid
            else: 
                right = mid
                
        return left + 1
        
        
        
        
        
            
        