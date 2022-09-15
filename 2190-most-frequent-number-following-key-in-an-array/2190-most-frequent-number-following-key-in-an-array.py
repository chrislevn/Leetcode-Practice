class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freqDict = {}
        temp, res = -1, 0
        for num in nums: 
            if num not in freqDict: 
                freqDict[num] = 1
            else: 
                freqDict[num] += 1

        for target in freqDict: 
            countTarget = 0
            for i in range(len(nums)-1): 
                if nums[i] == key and nums[i+1] == target: 
                    countTarget += 1
            if countTarget > temp: 
                res = target
                temp = countTarget

        return res