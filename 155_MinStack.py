__author__ = 'feng'

from util import *

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data =[]
        self.minindex = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.data) == 0:
            self.data.append(x)
            self.minindex.append(x)
        else:
            self.data.append(x)
            if x <= self.minindex[len(self.minindex)-1]:
                self.minindex.append(x)



    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.data):
            d = self.data.pop()
            if d == self.minindex[len(self.minindex)-1]:
                self.minindex.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.data[len(self.data)-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minindex[len(self.minindex)-1]


if __name__ == '__main__':
    s = MinStack()