class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        output = []

        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - i-1))

        num += 1

        while num > 0:
            digit = num % 10
            num //= 10

            output.append(digit)

        output.reverse()

        return output