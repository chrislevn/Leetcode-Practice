class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for r in mat:
            if sum(r) == 1:
                c = r.index(1)
                summ = 0
                for rw in range(len(mat)):
                    summ += mat[rw][c]

                if summ == 1:
                    ans += 1

        return ans