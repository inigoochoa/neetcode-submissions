class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        reps = {}
        for n in nums:
            if n not in reps:
                reps[n] = 0
            reps[n] += 1
        return sorted(reps, key=reps.get, reverse = True)[:k]
        
        