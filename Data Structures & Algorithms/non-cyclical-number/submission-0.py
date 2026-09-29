class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        current = sum([int(e) * int(e) for e in str(n)])
        while current not in visited and current != 1:
            visited.add(current)
            current = sum([int(e) * int(e) for e in str(current)])
        return True if current == 1 else False