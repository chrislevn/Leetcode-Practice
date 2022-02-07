class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        before, after = 0, sum(nums)

        for i in range(len(nums)):

            after -= nums[i]
            if before == after:
                return i
            before += nums[i]
        return -1