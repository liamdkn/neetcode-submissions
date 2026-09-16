class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for letter in s: 
            if letter in {'(','{','['}:
                stack.append(letter)
            if letter in {')','}',']'}:
                isEmpty = not bool(stack)
                if isEmpty : return False
                opening_bracket = stack.pop()
                if matching[letter] == opening_bracket:
                        pass
                else: return False
        isEmpty = not bool(stack)
        if isEmpty:
            return True
        return False