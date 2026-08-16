class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for w in s:
            if w in ("(", "{", "["):
                left.append(w)
                continue 

            if len(left) == 0:
                return False

            last = left.pop()
            if pairs[w] != last:
                return False

        return True if len(left) == 0 else False