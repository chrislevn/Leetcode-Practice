class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # fullList = [x for x in range(1, n+1)]
        
        result = []
        start = 1
        
        for i in range(len(target)):
            while target[i] != start: 
                result.append("Push")
                result.append("Pop")
                start += 1
            result.append("Push")
            start += 1
        return result