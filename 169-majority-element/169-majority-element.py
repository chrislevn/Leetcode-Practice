class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        check = len(nums) // 2
        
        for num in nums: 
            if num not in freq: 
                freq[num] = 1
            else:
                freq[num] += 1
                
        for item in freq: 
            if freq[item] > check: 
                return item
    
        