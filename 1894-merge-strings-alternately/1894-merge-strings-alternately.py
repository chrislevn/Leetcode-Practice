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
            resultText += word1[currIndex:]
        elif len(word1) < len(word2):
            resultText += word2[currIndex:]

        return resultText