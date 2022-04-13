class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        firstDict = {}
        secondDict = {}
        
        s1List = s1.split(" ")
        s2List = s2.split(" ")
        
        for char in s1List: 
            if char not in firstDict: 
                firstDict[char] = 1
            else: 
                firstDict[char] += 1
                
        for char in s2List: 
            if char not in secondDict: 
                secondDict[char] = 1
            else: 
                secondDict[char] += 1
        
        for item in firstDict: 
            if firstDict[item] == 1 and item not in secondDict: 
                result.append(item)
        
        for item in secondDict: 
            if secondDict[item] == 1 and item not in firstDict: 
                result.append(item)
        
        return result