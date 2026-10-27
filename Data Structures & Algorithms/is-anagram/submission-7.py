class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ord = sorted(s)
        t_ord = sorted(t)
        return s_ord == t_ord
