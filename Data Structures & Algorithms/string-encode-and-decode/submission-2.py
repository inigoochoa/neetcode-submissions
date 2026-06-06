class Solution:

    def encode(self, strs: List[str]) -> str:
        result1 = ""
        for word in strs:
            result1 = result1 + word + "|@@#@|@|"
        print(result1)
        return result1




    def decode(self, s: str) -> List[str]:
     return s.split("|@@#@|@|")[:-1]