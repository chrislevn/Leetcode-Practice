class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currMax = max(candies)
        result = []
        for i in range(len(candies)): 
            if candies[i] + extraCandies >= currMax: 
                # currMax = candies[i] + extraCandies
                result.append(True)
            else: 
                result.append(False)

        return result

