class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = int(len(nums))

        if l%2 == 0:
            print(1)
            n = int(nums[l//2-1]) + int(nums[l//2])
            print(n)
            if n/2 >= target:
                for i in range(0, l//2):
                    if nums[i] == target:
                        return i
                return -1
            for i in range(l//2, l):
                if nums[i] == target:
                    return i
            return -1

        if nums[l//2] == target:
            return l//2
        if nums[l//2] > target:
            print(2)
            for i in range(0, l//2+1):
                if nums[i] == target:
                    return i 
                return -1
        for i in range(l//2, l):
            if nums[i] == target:
                return i
        return -1