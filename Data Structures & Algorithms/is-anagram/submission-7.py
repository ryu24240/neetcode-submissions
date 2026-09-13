class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for s_char, t_char in zip(s, t):
            counts[ord(s_char) - ord("a")] += 1
            counts[ord(t_char) - ord("a")] -= 1

        for count in counts:
            if count != 0:
                return False
        return True
