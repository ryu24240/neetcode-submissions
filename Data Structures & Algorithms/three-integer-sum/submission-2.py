class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)-2):
            fixed_num = nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            if fixed_num > 0:
                break

            target_pair_sum = -fixed_num
            left = i + 1
            right = len(nums) - 1

            while left < right:
                pair_sum = nums[left] + nums[right]

                if pair_sum < target_pair_sum:
                    left += 1
                elif pair_sum > target_pair_sum:
                    right -= 1
                else:
                    output.append([
                        fixed_num,
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return output