class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashTable = dict()
        res = -1
        
        for num in nums: 
            if num not in hashTable: 
                hashTable[num] = 1
            else: 
                hashTable[num] += 1
                                
        for item, value in hashTable.items(): 
            if value == 1: 
                res = max(res, item)
                
        return res