class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        curr = 0
        res = 0
        
        for i in range(len(rungs)): 
            if (rungs[i] - curr) > dist: 
                res += (rungs[i] - curr - 1) // dist
            curr = rungs[i]
            
        return res
            