class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # b = sorted(b, reverse=True)
        # b = "".join(str(i) for i in b)
        # print(b)
        # res = pow(int(a), int(b))
        
        return (a % 1337)**(1140 + int(''.join(map(str, b))) % 1140) % 1337
     