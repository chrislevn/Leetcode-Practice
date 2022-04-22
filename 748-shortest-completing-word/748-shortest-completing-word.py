class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licenseDict = self.countFreq(licensePlate)
        length = len(licenseDict)
        wordList = []
        result = "jabdjbwsdklcnskdccsdcjnbscj"
        
        for word in words: 
            wordDict = self.countFreq(word)
            count = 0
            for value in licenseDict: 
                if value in wordDict:
                    if licenseDict[value] <= wordDict[value]: 
                        count += 1
            if count == length and len(result) > len(word):
                result = word
        return result
            
        
    def countFreq(self, word: str): 
        ignoreNumber = "0123456789 "
        wordDict = dict()
        
        for char in word: 
            char = char.lower()
            if char not in ignoreNumber:
                if char not in wordDict: 
                    wordDict[char] = 1
                else:
                    wordDict[char] += 1
        return wordDict