class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_char = 10000000
        for char in strs: 
            if len(char) < min_char: 
                min_char = len(char)
        
        res = ""
        i = 0 
        print(min_char)
        while i < min_char: 
            curr = strs[0][i]
            count = 0
            for letter in strs:
                if letter[i] == curr:
                    count += 1
                    
            if count == len(strs): 
                res += curr
            else: 
                break
            i += 1
            
        return res
            