class Solution:
    def totalMoney(self, n: int) -> int:
        divide_part = n // 7 
        remain = n % 7 
        
        result = 0
        for i in range(1, divide_part+1): 
            result += sum(range(i,i+7,1))
        
        result += sum(range((divide_part + 1), (divide_part + 1)+remain, 1))
        
        return result