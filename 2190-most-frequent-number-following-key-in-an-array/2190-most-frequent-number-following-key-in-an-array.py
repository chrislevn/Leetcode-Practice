class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freqDict = {}
        for i in range(len(nums)-1): 
            if nums[i] == key: 
                if nums[i+1] not in freqDict: 
                    freqDict[nums[i+1]] = 1
                else: 
                    freqDict[nums[i+1]] += 1
        return max(freqDict, key=freqDict.get)