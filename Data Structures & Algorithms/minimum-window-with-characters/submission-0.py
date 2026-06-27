class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_count, window = {}, {}

        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)

                window[s[l]] -= 1

                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""
                
            



        