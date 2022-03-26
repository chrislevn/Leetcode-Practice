class Solution:
    def minimumCost(self, cost: List[int]) -> int:
#         if len(cost) <= 2: 
#             return sum(cost)
#         cost = sorted(cost, reverse=True)
#         i, j, k = 0, 1, 2
#         curr_sum = 0
        
#         while k < len(cost): 
#             curr_sum += 
        return sum(cost) - sum(sorted(cost)[-3::-3])
            