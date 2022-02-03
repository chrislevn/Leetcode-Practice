class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        startValue = 0 
        for operation in operations: 
            if "+" in operation:
                startValue += 1
            else: 
                startValue -= 1
        return startValue