class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        return s_sorted == t_sorted

        '''for i, letter in enumerate(s_sorted):
            if letter != t_sorted[i]:
                return False
        return True '''
            