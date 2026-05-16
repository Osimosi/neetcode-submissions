class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {} #char : count

        for s in magazine:
            map[s] = 1 + map.get(s,0)

        for c in ransomNote:
            if map.get(c, 0) > 0:
                map[c] -= 1 
            else:
                return False
        return True