class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counters = dict()
        for e in s:
            if e not in counters:
                counters[e] = 1
            else:
                counters[e] += 1
        
        for e in t:
            if e not in counters:
                return False
            else:
                counters[e] -= 1
            
            if counters[e] < 0:
                return False

        for c in counters:
            if counters[c] != 0:
                return False
        return True