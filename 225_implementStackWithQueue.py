__author__ = 'feng'

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack =[]
        self.outStack =[]


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.outStack) == 0:
            while len(self.inStack):
                self.outStack.append(self.inStack.pop())
        self.outStack.pop()



    def top(self):
        """
        :rtype: int
        """
        if len(self.outStack) == 0:
            while len(self.inStack):
                self.outStack.append(self.inStack.pop())
        return self.outStack[len(self.outStack)-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.inStack) == 0 and len(self.outStack) == 0

if __name__ == '__main__':
    s = Stack()