class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AABCDEEEAAEEAA

        k = 1
        """
        l = 0
        r = 0
        frequency_count = {}
        max_length = 0 

        while r < len(s) - 1 and l < len(s) - 1:
            print("loop")
            if s[l] not in frequency_count:
                frequency_count[s[l]] = 1
            r += 1
            if s[r] not in frequency_count:
                frequency_count[s[r]] = 1
            else:
                frequency_count[s[r]] += 1
            print(frequency_count)
            length = r - l + 1
            max_frequency = max(list(frequency_count.values()))
            if length - max_frequency <= k: # tells us we have a valid length
                if length > max_length:
                    max_length = length
            while k < length - max_frequency and l < len(s):
                frequency_count[s[l]] -= 1
                l += 1
                length -= 1
                max_frequency = max(list(frequency_count.values()))
            print(l)

        return max_length    



        