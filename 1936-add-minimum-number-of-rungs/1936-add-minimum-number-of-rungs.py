class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        curr, res = 0, 0
        length = len(rungs)
        
        for i in range(length): 
            if (rungs[i] - curr) > dist: 
                res += (rungs[i] - curr - 1) // dist
            curr = rungs[i] 
        return res
            