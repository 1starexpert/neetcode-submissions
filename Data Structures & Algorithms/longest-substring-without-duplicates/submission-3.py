class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        proper solution:

        abcddbcdabcd
        """
        l = 0
        r = 0
        max_length = 0
        window = set()

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                # r += 1
                length = r - l + 1
                r += 1
                if length > max_length: 
                    max_length = length
            else:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1

        return max_length
                


        