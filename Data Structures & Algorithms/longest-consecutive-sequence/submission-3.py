class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for n in num_set:
            if n-1 not in num_set:
                curr_length = 1
                while n+1 in num_set:
                    curr_length += 1
                    n+=1
                max_length = max(curr_length, max_length)
        return max_length