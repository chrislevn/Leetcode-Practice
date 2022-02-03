import numpy as np
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i <= len(arr):
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1

        l1 = [ d.get(i, 0) for i in range(1, len(arr))]
        diff = np.cumsum(l1) - np.array([ i for i in range(1, len(arr))])

        return int(len(arr)-max(np.append(diff, [0])))