class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''

        min_word_length = len(strs[0])
        for word in strs:
            if len(word) < min_word_length:
                min_word_length = len(word)
            
        for i in range(min_word_length):
            letter = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != letter:
                    return common
            common += letter
        return common