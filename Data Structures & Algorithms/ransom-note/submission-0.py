class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}

        for char in magazine:
            map[char] = 1 + map.get(char, 0)


        for char in ransomNote:
            if map.get(char, 0) > 0:
                map[char] -=1
            else:
                return False
            
        return True
        