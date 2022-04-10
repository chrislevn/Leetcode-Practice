class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        length = len(s)
        if length < 3: 
            return []
        else: 
            ans = []
            i = 0 
            for j in range(length):
                if j == length - 1 or s[j] != s[j+1]:
                    if j-i+1 >= 3:
                        ans.append([i, j])
                    i = j+1
            return ans

        