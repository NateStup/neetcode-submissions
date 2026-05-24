class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for i in range(len(words)):
                if words[i].find(word) != -1 and word != words[i]:
                    result.append(word)
                    break
        return result