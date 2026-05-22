class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        found_word = False
        for i in range(len(s) - 1, -1, -1):
            string = s[i]
            if string == " " and found_word == True:
                break
            elif string != " ":
                length += 1
                found_word = True

        
        return length

