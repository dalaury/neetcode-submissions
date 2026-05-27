class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = ["(","{","["]
        close_braces = [")","}","]"]

        def isPair(s1: str, s2: str) -> bool:
            valid_pair = False

            if s1 == "(" and s2 == ")":
                valid_pair = True
            elif s1 == "[" and s2 == "]":
                valid_pair = True
            elif s1 == "{" and s2 == "}":
                valid_pair = True

            return valid_pair
        
        if len(s) <= 1:
            return False

        check_stack = []
        
        for brace in s:
            if len(check_stack) == 0 and brace in close_braces:
                return False
            elif brace in open_braces:
                check_stack.append(brace)
            elif isPair(check_stack[-1], brace):
                check_stack.pop()
            else:
                return False

        if len(check_stack) == 0:
            return True
        
        return False