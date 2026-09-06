class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0

        nums.sort()
        # print(nums)

        for i in range(len(nums)+1):

            if i not in nums:
                return i

            # count += 1