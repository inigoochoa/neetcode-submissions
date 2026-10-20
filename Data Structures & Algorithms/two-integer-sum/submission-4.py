class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i + 1, num_len):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result
