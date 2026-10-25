class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        longest_length = 0

        for right, character in enumerate(s):
            counts[character] = counts.get(character, 0) + 1

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            longest_length = max(
                longest_length,
                right - left + 1,
            )

        return longest_length

        