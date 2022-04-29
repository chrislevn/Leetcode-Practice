class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        try:
            for i in range(len(words)):
                for j in range(len(words[i])):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except IndexError:
            return False