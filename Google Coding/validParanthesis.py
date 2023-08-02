class Solutions:
    def validParanthesis(self, lists:list[str])->bool:
        stack = []
        closetoOpen = {" )":" (", "} ":" {","] ":" ["}
        for c in lists:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                     return False
            else:
                 stack.append(c)
        return True if not stack else False

checker = Solutions()
print(checker.validParanthesis(["[","["]))