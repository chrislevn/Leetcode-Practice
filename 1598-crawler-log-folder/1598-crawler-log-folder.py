class Solution:
    def minOperations(self, logs: List[str]) -> int:
        start = 0 
        for log in logs: 
            if log == "../" and start > 0: 
                start -= 1
            elif log[0] != ".": 
                start += 1
            elif log == "./": 
                continue
            
        return start
            