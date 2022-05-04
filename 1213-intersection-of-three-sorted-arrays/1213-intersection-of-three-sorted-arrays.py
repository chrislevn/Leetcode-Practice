class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        for num in arr1: 
            if self.binarySearch(0, len(arr2), arr2, num) and self.binarySearch(0, len(arr3), arr3, num): 
                result.append(num)
        return result
    
        
    def binarySearch(self, left, right, arr, value):
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == value: 
                return True
            elif value > arr[mid]: 
                left = mid+1
            else: 
                right = mid
                
        return False