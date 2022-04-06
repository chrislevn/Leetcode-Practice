class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        while not self.checkNum(startValue, nums): 
            startValue += 1
        return startValue
        
    def checkNum(self, startValue, nums: List[int]) -> bool:
        """Calculate value after iterating through the nums value. 
        
        Args: 
            startValue (int): starting value. 
            nums (list): list of integers. 
            
        Returns: 
            Whether the result value meets the requirement.

        """
        
        for i in range(len(nums)): 
            startValue += nums[i]
            if startValue < 1: 
                return False
        return True
        