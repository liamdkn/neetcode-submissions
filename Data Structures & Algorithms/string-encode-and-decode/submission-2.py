class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

         
        


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            start = j+1
            res.append(s[start:start+length])
            i = start+length
        return res