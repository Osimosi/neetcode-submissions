class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {} # char : count

        # building hashmap
        for c in s:
            counts[c] = 1 + counts.get(c,0)

        for c in t:
            if counts.get(c,0) > 0:
                counts[c]-=1
            else:
                return False
        return True