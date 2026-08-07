class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        return any(num in visited or visited.add(num) for num in nums)