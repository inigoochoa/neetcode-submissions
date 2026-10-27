class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for S in s:
            if S in s_dict:
                s_dict[S] += 1
            else:
                s_dict[S] = 1
            
        for T in t:
            if T in t_dict:
                t_dict[T] += 1
            else:
                t_dict[T] = 1
        return s_dict == t_dict
