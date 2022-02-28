class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        check_dict = {}
        for i in range(1, len(edges)+2): 
            check_dict[i] = []
        
        for edge in edges: 
            check_dict[edge[0]].append(edge[1])
            check_dict[edge[1]].append(edge[0])
        
        for key in check_dict: 
            if len(check_dict[key]) == len(edges): 
                return key 
            
        