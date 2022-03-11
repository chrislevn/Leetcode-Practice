class Solution:
    def removeVowels(self, s: str) -> str:
        check = {'a', 'e', 'i', 'o', 'u'}
        result = ""
        
        for i in range(len(s)): 
            if s[i] not in check:
                result += s[i]
                
        return result
                