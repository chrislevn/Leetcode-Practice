class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        digit = int(''.join([str(i) for i in num]))
        return [int(d) for d in str((digit + k))]