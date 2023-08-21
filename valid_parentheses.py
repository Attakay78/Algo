from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, item):
        self.container.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        open_parens = ['(', '{', '[']
        close_parens = [')', '}', ']']

        for paren in s:
            if paren in open_parens:
                stack.push(paren)
            else:
                last_item = stack.pop()

                if last_item is None:
                    return False
                
                if open_parens.index(last_item) != close_parens.index(paren):
                    return False

        return True if stack.is_empty() else False


s = Solution()
res = s.isValid("[{}()]")
print(res)
