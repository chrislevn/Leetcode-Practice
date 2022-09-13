class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pre, res = 0, 0
        length = len(rungs)
        
        for i in range(length): 
            res += (rungs[i] - pre - 1) // dist
            pre = rungs[i]
        
        return res
            