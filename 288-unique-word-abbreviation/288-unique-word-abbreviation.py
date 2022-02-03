class ValidWordAbbr:

    def __init__(self, dictionary):
        self.dic = collections.defaultdict(set)
        for s in dictionary:
            val = s
            n = len(s)
            if n > 2:
                s = s[0]+str(n-2)+s[-1]
            self.dic[s].add(val)

    def isUnique(self, word):
        val = word 
        n = len(word)
        if n > 2:
            word = word[0]+str(n-2)+word[-1]
        return len(self.dic[word]) == 0 or (len(self.dic[word]) == 1 and val == list(self.dic[word])[0])


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)