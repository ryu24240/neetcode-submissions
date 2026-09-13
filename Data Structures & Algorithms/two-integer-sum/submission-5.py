class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        if len(nums) == 2:
            return [0, 1]

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in counts:
                return [counts[remainder], i]

            if num not in counts:
                counts[num] = nums.index(num)
