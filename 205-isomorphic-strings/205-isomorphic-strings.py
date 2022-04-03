class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        print(self.checkString(s), "\n", self.checkString(t))
        return self.checkString(s) == self.checkString(t)
        
    def checkString(self, string): 
        check = {}
        start = 'a'
        result = ""
        
        for char in string: 
            if char not in check: 
                check[char] = start
                start = chr(ord(start)+1)
            result += str(check[char])
        return result