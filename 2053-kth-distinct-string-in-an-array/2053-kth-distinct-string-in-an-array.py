class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        checkDict = {}
        table = []
        
        for word in arr: 
            if word not in checkDict: 
                checkDict[word] = 1
            else:
                checkDict[word] += 1
        
        i = 1
        for value in checkDict: 
            if checkDict[value] == 1:
                if i == k: 
                    return value
                else:
                    i += 1
        return ""
        
        