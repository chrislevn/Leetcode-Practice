class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        
        return self.countVowels(a) == self.countVowels(b)
        
        
    def countVowels(self, s: str) -> int: 
        dict = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for char in s: 
            if char.lower() in dict: 
                count += 1
        return count