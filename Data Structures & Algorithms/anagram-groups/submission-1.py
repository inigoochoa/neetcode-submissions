class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicc = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dicc:
                dicc[key].append(s)
            else:
                dicc[key] = [s]
        return list(dicc.values())