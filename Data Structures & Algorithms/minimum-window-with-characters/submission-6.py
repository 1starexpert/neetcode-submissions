class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        table_s = {a: 1, b: 2, c: 3}
        table_t = {a: 1, b: 2, d: 4}
        """
        def helper(table_s: dict, table_t: dict) -> bool:
            for key, value in table_t.items():
                if table_s.get(key, 0) < value:
                    return False
            return True
        """
        """
        # edge case:
        if len(s) < len(t):
            return ""
        if s == t:
            return s

        t_table = {}
        substring_table = {}
        substring = ""
        min_substring = ""

        for letter in t:
            if letter not in t_table:
                t_table[letter] = 1
            else:
                t_table[letter] += 1

        # sliding window algorithm here:
        l = 0
        r = 0

        substring_table[s[0]] = 1 # first window element
        substring += s[0]

        if substring_table == t_table:
            return substring
        print("executed")
        while l < len(s) - 1:

            #print(substring)
            if not helper(substring_table, t_table) and r < len(s) - 1:
                #print("if not")
                r += 1
                letter = s[r]
                if letter in substring_table:
                    substring_table[letter] += 1
                else: 
                    substring_table[letter] = 1
                substring += letter

            # tighten the window:
            if helper(substring_table, t_table):
                if min_substring == "":
                    min_substring = substring
                else:
                    if len(substring) < len(min_substring):
                        min_substring = substring
                letter = s[l]
                l += 1
                substring = substring[1:]
                substring_table[letter] -= 1
            #print(substring_table)
            #print(t_table)
            #print(substring)
            #print(f"Value of r pointer is: {r} Value of l is {l}")
            if r == len(s) - 1 and not helper(substring_table, t_table):
                letter = s[l]
                l += 1
                substring = substring[1:]
                substring_table[letter] -= 1
        #print("teriminate")
        if helper(substring_table, t_table) and len(substring) < len(min_substring):
            min_substring = substring
        return min_substring
            





