class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digits = len(digits)
        num = int("".join([str(e) for e in digits]))
        if len(str(num + 1)) > num_digits:
            return [1] + [0] * num_digits
        else:
            return [int(e) for e in str(num + 1)]