from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for palabra in strs:
            result["".join(sorted(palabra))].append(palabra)
            
        return list(result.values())