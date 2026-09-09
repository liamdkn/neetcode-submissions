class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        
        for word in strs:
            sorted_string = ''.join(sorted(word))

            if sorted_string in dictionary:
                dictionary[sorted_string].append(word)
            else:
                dictionary[sorted_string] = [word]

        return list(dictionary.values())
