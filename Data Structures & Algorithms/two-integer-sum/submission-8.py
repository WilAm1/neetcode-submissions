class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 0
        idx = 0
        for num1 in range(0, len(nums)):
            left = nums[num1]
            for num2 in range(idx, len(nums)):
                if idx == num2:
                    continue
                right = nums[num2]
                theSum = left + right
                if theSum  == target:
                    return [num1, num2]
            idx += 1