class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            n = target - nums[i]
            if n in hashMap:
                return [hashMap[n], i]
            hashMap[nums[i]] = i 
        return
        