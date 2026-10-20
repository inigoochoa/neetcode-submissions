class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valores = set()
        for i in nums:
            if i in valores:
                return True
            valores.add(i)
        return False