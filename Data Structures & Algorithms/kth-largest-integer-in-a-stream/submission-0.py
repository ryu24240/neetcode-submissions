class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.index = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.index-1]
