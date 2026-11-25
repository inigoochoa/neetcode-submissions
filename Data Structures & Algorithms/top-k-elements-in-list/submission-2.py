from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for numero in nums:
            result[numero] += 1
        lista = sorted(result.keys(), key=result.get, reverse=True)
        return lista[:k]