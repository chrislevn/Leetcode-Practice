import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        firstLen = len(str1)
        secondLen = len(str2)

        numericalGCD = math.gcd(firstLen, secondLen)  

        if str1[:numericalGCD] * (firstLen // numericalGCD) != str1 or str2[:numericalGCD] * (secondLen // numericalGCD) != str2: 
            return ""
        else: 
            if str1[:numericalGCD] != str2[:numericalGCD]: 
                return ""
            else: 
                return str1[:numericalGCD]
