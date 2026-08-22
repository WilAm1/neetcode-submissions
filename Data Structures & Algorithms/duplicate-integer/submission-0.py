class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = {}
        for number in nums:
            if number in hasSeen:
                print(number)
                return True
            else:
                print(f'number is {number}')
                hasSeen[number] = 1
        return False
            