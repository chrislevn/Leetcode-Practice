class Solution:
    def isBoomerang(self, P: List[List[int]]) -> bool:
        x1=P[0][0]
        x2=P[1][0]
        x3=P[2][0]
        y1=P[0][1]
        y2=P[1][1]
        y3=P[2][1]
        
        delta=x1*(y2-y3)-y1*(x2-x3)+(x2*y3-y2*x3)
        return delta!=0
        