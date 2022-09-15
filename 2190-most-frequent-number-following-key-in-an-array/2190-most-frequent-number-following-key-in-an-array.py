class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freqDict = {}
        temp, res = -1, 0
        for i in range(len(nums)-1): 
            if nums[i] == key: 
                if nums[i+1] not in freqDict: 
                    freqDict[nums[i+1]] = 1
                else: 
                    freqDict[nums[i+1]] += 1
                if freqDict[nums[i+1]] > temp: 
                    temp = freqDict[nums[i+1]]
                    res = nums[i+1]
        return res