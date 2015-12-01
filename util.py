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
    while i < len(l) and len(p):
        pp = []
        for j in xrange(0, len(p)):
            if l[i] == '#':
                p[j].left = None
            else:
                p[j].left = TreeNode(int(l[i]))
                pp.append(p[j].left)
            i+= 1

            if l[i] == '#':
                p[j].right = None
            else:
                p[j].right = TreeNode(int(l[i]))
                pp.append(p[j].right)
            i += 1
        p = pp
    return root


