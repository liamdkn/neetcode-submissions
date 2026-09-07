class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictionary = {}

        if(len(s) != len(t)):
            return False
        
        for letter in s:
            dictionary[letter] = dictionary.get(letter,0) +1
            
        for letter2 in t:
            if dictionary.get(letter2, 0) > 0:
                dictionary[letter2] -=1
            else:
                return False 
        return True

