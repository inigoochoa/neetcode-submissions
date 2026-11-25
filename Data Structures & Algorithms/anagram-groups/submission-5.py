from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for palabra in strs:
            #if ''.join(sorted(palabra)) in result:
            #    result[''.join(sorted(palabra))].append(palabra)
            #else:
            #    result[''.join(sorted(palabra))] = [palabra]
        #return list(result.values())
            result["".join(sorted(palabra))].append(palabra)
        return list(result.values())