class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        result = []
        if length % k == 0: 
            for i in range(k, length+1, k):
                result.append(s[i-k:i])
            return result
        else:
            remain = length // k
            count = 0
            for i in range(k, (remain * k)+1, k):
                result.append(s[i-k:i])
                count = i
                
            new_letter = s[count:] + fill*((remain+1)*k-length)
            result.append(new_letter)
            return result
        