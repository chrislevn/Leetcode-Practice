import queue

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "u", "i", "o"]
        nonvowels = []
        result = ""
        q = []

        for char in s: 
            if char.lower() not in vowels: 
                nonvowels.append(char)
            else: 
                nonvowels.append("_")
                q.append(char)

        for i in range(len(s)): 
            if s[i].lower() not in vowels: 
                result += nonvowels[i]
            else: 
                temp = q.pop()
                result += temp

        return result

        