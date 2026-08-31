class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordsDict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in wordsDict:
                wordsDict[sorted_word] = [word]
            else:
                wordsDict[sorted_word].append(word)
        return list(wordsDict.values())

                