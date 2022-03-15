class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        select_index = 0
        count = 0
        if ruleKey == "type": 
            select_index = 0
        elif ruleKey == "color": 
            select_index = 1
        else: 
            select_index = 2
            
        for item in items: 
            if item[select_index] == ruleValue: 
                count += 1
        return count
 