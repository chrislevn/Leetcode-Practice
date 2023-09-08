class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLength = min(len(word1), len(word2))
        resultText = ""
        currIndex = 0
        for index in range(minLength): 
            resultText += word1[index] + word2[index]
            currIndex = index

        currIndex += 1
        if len(word1) > len(word2): 
            while currIndex < len(word1): 
                resultText += word1[currIndex]
                currIndex += 1
        elif len(word1) < len(word2):
             while currIndex < len(word2): 
                resultText += word2[currIndex]
                currIndex += 1

        return resultText