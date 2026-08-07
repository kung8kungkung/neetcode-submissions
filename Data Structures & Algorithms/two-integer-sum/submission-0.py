class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in visited:
                return [visited[remaining], i]
            visited[num] = i
        return [-1, -1]