class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            try:
                j = nums.index(target - num, i + 1)
                return [i, j]
            except ValueError:
                continue

