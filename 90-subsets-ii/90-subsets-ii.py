class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.backtrack(nums, [], 0)
        return self.res
    
    def backtrack(self, nums, currentArray, start): 
        self.res.append(currentArray)
        if start > len(nums): 
            return 
        for i in range(start, len(nums)): 
            if i  > start and nums[i-1] == nums[i]: 
                continue 
            self.backtrack(nums, currentArray + [nums[i]], i+1)