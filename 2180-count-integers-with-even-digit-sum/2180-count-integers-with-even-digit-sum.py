class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num+1): 
            if sum([int(d) for d in str(i)]) % 2 == 0: 
                count += 1
        return count
        