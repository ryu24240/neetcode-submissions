class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters_in_windows = set()
        left = 0
        longest_length = 0

        for right, character in enumerate(s):
            while character in characters_in_windows:
                characters_in_windows.remove(s[left])
                left += 1

            characters_in_windows.add(character)

            window_length = right - left + 1
            longest_length = max(longest_length, window_length)

        return longest_length 