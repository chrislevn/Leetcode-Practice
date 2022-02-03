class Solution:
    def replaceDigits(self, s: str) -> str:
        check_digit = "0123456789"
        s = list(s)
        for i in range(len(s)): 
            if s[i] in check_digit: 
                s[i] = chr(ord(s[i-1]) + int(s[i]))
        return "".join(s)
        