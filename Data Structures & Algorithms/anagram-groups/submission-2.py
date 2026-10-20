class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for s in strs:
            clave = "".join(sorted(s))
            if clave in solution.keys():
                solution[clave].append(s)
            else:
                solution[clave] = [s]
        return list(solution.values())