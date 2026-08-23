class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for letter in s:
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1
        for letter in t:
            if letter not in map:
                return False
            map[letter] -=1
            if map[letter] < 0:
                return False
        for value in map.values():
            if value > 0:
                return False
        return True