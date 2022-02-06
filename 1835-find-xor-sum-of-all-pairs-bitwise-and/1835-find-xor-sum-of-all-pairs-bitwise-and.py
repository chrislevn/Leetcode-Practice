class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:   
        ans1,ans2=0,0
        for i in arr1: ans1^=i
        for i in arr2: ans2^=i
        return ans1 & ans2
        