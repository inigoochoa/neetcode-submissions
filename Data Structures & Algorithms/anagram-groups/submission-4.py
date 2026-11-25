class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for palabra in strs:
            if ''.join(sorted(palabra)) in result:
                result[''.join(sorted(palabra))].append(palabra)
            else:
                result[''.join(sorted(palabra))] = [palabra]
        return list(result.values())
