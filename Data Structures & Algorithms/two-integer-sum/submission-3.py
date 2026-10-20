class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        for i in range(num_len):
            for j in range(1, num_len - i):
                if nums[i] + nums[i+j] == target:
                    result = [i, i+j]
                    return result
