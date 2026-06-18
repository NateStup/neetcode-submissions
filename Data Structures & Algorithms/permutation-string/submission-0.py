class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        if len(s1) > len(s2):
            return False
        else:
            req_freq = {}
            for char in s1:
                req_freq[char] = 1 + req_freq.get(char, 0)
        
        for r in range(len(s1) - 1, len(s2)):
            cur_freq = {}
            for j in range(l, r + 1):
                cur_freq[s2[j]] = 1 + cur_freq.get(s2[j], 0)
            if cur_freq == req_freq:
                return True
            l += 1

        return False