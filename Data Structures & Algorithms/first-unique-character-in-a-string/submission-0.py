class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}

        for letter in s:
            char_count[letter] = char_count.get(letter, 0) + 1

        for i, letter in enumerate(s):
            if char_count[letter] == 1:
               return i
        return -1