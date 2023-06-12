class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map = {}
        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in check_map: 
                return [i, check_map[diff]]
            check_map[nums[i]] = i

         