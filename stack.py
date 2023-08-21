# Stack implementation using one queue
# Reverse a string using a stack

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, item):
        self.container.append(item)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def reverse(self, s):
        for ch in s:
            self.push(ch)
        
        res = ""
        for _ in range(len(self.container)):
            res += self.pop()
        
        return res


stack = Stack()
print(stack.reverse("clown"))



# Stack implementation using two queues
class MyStack:

    def __init__(self):
        self.front_queue = deque()
        self.back_queue = deque()

    def push(self, x: int) -> None:
        self.front_queue.append(x)

    def pop(self) -> int:
        self.top()
        return self.back_queue.pop()

    def top(self) -> int:
        if len(self.front_queue) != 0:
            while self.front_queue:
                self.back_queue.append(self.front_queue.popleft())
        
        return self.back_queue[-1]

    def empty(self) -> bool:
        return len(self.front_queue) == 0 and len(self.back_queue) == 0



# Queue implementation using stack (stack can be implemented by just a list, so we are using two lists here)
class MyQueue:

    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        self.back_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.front_stack.pop()

    def peek(self) -> int:
        if not self.front_stack:
            while self.back_stack:
                self.front_stack.append(self.back_stack.pop())
        
        return self.front_stack[-1]
        
    def empty(self) -> bool:
        return not self.front_stack and not self.back_stack
