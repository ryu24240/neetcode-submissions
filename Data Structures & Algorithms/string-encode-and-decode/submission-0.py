class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_text = ""
        for element in strs:
            length = str(len(element))
            encoded_text += length + "#" + element

        print(f"encoded_text: {encoded_text}")
        return encoded_text

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            delimiter_index = s.find("#", i)

            length = int(s[i:delimiter_index])

            text_start = delimiter_index + 1
            text_end = text_start + length

            result.append(s[text_start:text_end])

            i = text_end

        return result

