class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alphabet = {}
        string = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(widths)): 
            alphabet[string[i]] = widths[i]
            
        curr = 0 
        count = 1 
        
        for i in range(len(s)): 
            if curr + alphabet[s[i]] <= 100: 
                curr += alphabet[s[i]]
            else: 
                curr = alphabet[s[i]]
                count += 1
        
        return [count, curr]