class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashRotate = {"6":"9", "9":"6", "8":"8", "0":"0", "1":"1"}
        newLetter = ""
        if len(num) == 1: 
            if num == "0" or num == "8" or num == "1": 
                return True
            else: 
                return False

        for i in range(len(num)-1, -1, -1): 
            if num[i] in hashRotate: 
                newLetter += hashRotate[num[i]]
            else: 
                return False
                newLetter += num[i]
        return newLetter == num
        
        