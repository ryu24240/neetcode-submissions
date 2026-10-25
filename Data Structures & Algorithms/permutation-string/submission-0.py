class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        window_counts = [0] * 26

        for letter in s1:
            index = ord(letter) - ord("a")
            s1_counts[index] += 1

        left = 0

        for right, letter in enumerate(s2):
            index = ord(letter) - ord("a")
            window_counts[index] += 1

            if right - left + 1 > len(s1):
                index = ord(s2[left]) - ord("a")
                window_counts[index] -= 1
                left += 1

            if window_counts == s1_counts:
                return True

        return False


        