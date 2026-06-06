class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # Creamos el hash map y revisamos si está antes:
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            dic[n] = i

 


         

