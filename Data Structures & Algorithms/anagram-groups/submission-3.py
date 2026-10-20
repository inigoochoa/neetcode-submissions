class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for i in strs:
            clave = "".join(sorted(i))
            if clave in solution.keys():
                solution[clave].append(i)
            else:
                solution[clave] = [i]
        return list(solution.values())
