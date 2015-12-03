__author__ = 'feng'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructTree(str):
    l = str.split(",")
    if l[0] == '#':
        return None
    root = TreeNode(int(l[0]))
    p = [root]
    i = 1
    while len(p)  and i < len(l):
        q = []
        for j in xrange(0, len(p)):
            if i < len(l) and l[i] != '#':
                p[j].left = TreeNode((int)(l[i]))
                q.append(p[j].left)
            i += 1
            if i < len(l) and l[i] != '#':
                p[j].right = TreeNode(int(l[i]))
                q.append(p[j].right)
            i += 1
        p = q
    return root


    return root

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
