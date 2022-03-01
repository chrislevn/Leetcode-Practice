class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([pow(x, 2) for x in nums])