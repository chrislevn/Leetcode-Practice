class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        checkSet = set(['b', 'a', 'l', 'l', 'o', 'o', 'n'])
        s = {'b':0, 'a':0, 'l':0, 'o':0, 'o':0, 'n':0}
        for char in text: 
            if char in checkSet: 
                s[char] += 1
        
        s['l'] //= 2
        s['o'] //= 2
        
        return min(s.values())