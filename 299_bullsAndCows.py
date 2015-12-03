__author__ = 'feng'

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        flag=[]
        mm ={}
        a = 0
        b= 0
        for i in xrange(0, len(secret)):
            if secret[i] == guess[i]:
                flag.append(1)
                a += 1
            else:
                flag.append(0)
                if secret[i] not in mm:
                    mm[secret[i]]  = 0
                mm[secret[i]] += 1
        #print mm

        for i in xrange(0, len(secret)):
            if flag[i] == 0 and guess[i] in mm:
                mm[guess[i]] -= 1
                b += 1
                if mm[guess[i]] == 0:
                    mm.pop(guess[i])
        return str(a) + "A" + str(b) + "B"

if __name__ == '__main__':
    s = Solution()
    print s.getHint("1123", "0111")