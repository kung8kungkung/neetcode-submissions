class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for w in s:
            if w in ("(", "{", "["):
                left.append(w)
            else:
                if len(left) == 0:
                    return False
                if w == ')':
                    last = left.pop()
                    if last != "(":
                        return False
                elif w == '}':
                    last = left.pop()
                    if last != "{":
                        return False
                elif w == ']':
                    last = left.pop()
                    if last != "[":
                        return False
        return True if len(left) == 0 else False