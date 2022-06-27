class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp = [0] * 1005
        for slot in trips:   
            for i in range(slot[1], slot[2]+1): 
                temp[i] += slot[0]
                if i == slot[2]: 
                    temp[i] -= slot[0]
                
                if temp[i] > capacity: 
                    return False
        return True