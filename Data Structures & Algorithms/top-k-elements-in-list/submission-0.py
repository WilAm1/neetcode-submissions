class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1

        # get the list of values sorted from highest to lowest
        sortedResult = sorted(numDict, key=numDict.get, reverse=True)
        return sortedResult[:k]