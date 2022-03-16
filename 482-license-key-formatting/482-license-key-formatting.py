class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        string_length = len(s)
        
        if string_length == 1: 
            if s != "-":
                return s.upper()
            else: 
                return ""
        
        letter = ""
        for char in s: 
            if char != "-": 
                letter += (char.upper())
                
        divide = len(letter) // k
        remain = len(letter) % k
        curr_index = 0
        result = []
        temp = ""
        
        for i in range(remain): 
            temp += letter[i]
            curr_index += 1
            
        if remain > 0: 
            result.append(temp)
        
        for i in range(divide): 
            temp = ""
            for j in range(k): 
                temp += letter[curr_index]
                curr_index += 1
            result.append(temp)
            
        # print(result)
        return "-".join(result)
            
        