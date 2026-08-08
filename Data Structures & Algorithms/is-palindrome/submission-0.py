class Solution:
    def to_check(self, s: str):
        code_point = ord(s)
        return (code_point >= 97 and code_point <= 122) or (code_point >= 65 and code_point <= 90) or (code_point >= 48 and code_point <= 57)

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while not self.to_check(s[i]) and i < j:
                i += 1
            while not self.to_check(s[j]) and i < j:
                j -= 1
            if i >= j:
                return True
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            
        