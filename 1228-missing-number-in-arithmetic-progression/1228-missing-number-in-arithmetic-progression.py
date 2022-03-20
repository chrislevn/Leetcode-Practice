class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        length = len(arr)
        diff = (arr[-1] - arr[0]) // length
        left, right = 0, length - 1
        
        while left < right: 
            mid = (left + right) // 2
            if arr[mid] == arr[0] + mid*diff: 
                left = mid + 1
            else: 
                right = mid
        return arr[0] + diff * left