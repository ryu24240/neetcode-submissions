class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        two_steps_before = 1
        one_steps_before = 2

        for _ in range(3, n+1):
            two_steps_before, one_steps_before =  one_steps_before, two_steps_before + one_steps_before

        return one_steps_before