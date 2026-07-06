class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Immediate brute force idea: 
        hash s1
        then check all substring hashes of s2 to see if
        it has matching
        """
        if len(s1) > len(s2):
            return False
        s1_frequency = {}
        s2_frequency = {}
        for letter in s1:
            if letter in s1_frequency:
                s1_frequency[letter] += 1
            else:
                s1_frequency[letter] = 1
        
        l = 0
        r = len(s1) - 1

        for i in range(len(s1)):
            if s2[i] not in s2_frequency:
                s2_frequency[s2[i]] = 1
            else:
                s2_frequency[s2[i]] += 1
        print(f"s1_frequency: {s1_frequency}")
        print(f"s2_frequency: {s2_frequency}")
        if s1_frequency == s2_frequency:
            return True
        while l < len(s2) - 1 and r < len(s2) - 1:
            print(f"s1_frequency: {s1_frequency}")
            print(f"s2_frequency: {s2_frequency}")
            if s1_frequency == s2_frequency:
                return True
            
            s2_frequency[s2[l]] -= 1
            if s2_frequency[s2[l]] == 0:
                del s2_frequency[s2[l]]
            l += 1
            r += 1
            if s2[r] in s2_frequency:
                s2_frequency[s2[r]] += 1
            else:
                s2_frequency[s2[r]] = 1
            print(f"s1_frequency: {s1_frequency}")
            print(f"s2_frequency: {s2_frequency}")
            if s1_frequency == s2_frequency:
                return True
        return False


