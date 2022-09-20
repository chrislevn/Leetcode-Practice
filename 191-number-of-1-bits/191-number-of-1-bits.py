class Solution:
    def hammingWeight(self, n: int) -> int:
        sumCheck = 0 
        while n != 0: 
            sumCheck += 1
            n &= (n-1)
        return sumCheck