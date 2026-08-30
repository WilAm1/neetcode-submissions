class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 0
        idx = 0
        for num1 in range(0, len(nums)):
            left = nums[num1]
            if left >= target:
                continue
            for num2 in range(1, len(nums) - idx):
                right = nums[num2]
                print(left,right,idx)
                if left + right == target:
                    return [num1, num2]
            idx += 1