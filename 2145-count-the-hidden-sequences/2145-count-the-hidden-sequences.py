class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        diff = list(accumulate(diff, initial = 0))
        return max(0, upper - lower - (max(diff) - min(diff)) + 1)

            
                    
                
        
        