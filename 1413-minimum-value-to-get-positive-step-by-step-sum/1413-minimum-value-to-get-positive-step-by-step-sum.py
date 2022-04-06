class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sumValue = 0
        minSum = 0
        
        for i in nums: 
            sumValue += i 
            minSum = min(minSum, sumValue)
            
        return 1 - minSum
        
        