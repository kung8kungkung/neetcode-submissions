class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def cal(m) -> int:
            return sum([int(e) * int(e) for e in str(m)])

        current = cal(n)
        while current not in visited and current != 1:
            visited.add(current)
            current = cal(current)
        return True if current == 1 else False