class Stack:
    def __init__(self):
        self._stack = []

    def push(self, num):
        self._stack.append(num)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def display(self):
        return self._stack[:]
