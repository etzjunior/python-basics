class Solution(object):
    def reverseString(self, s):
        pos1 = 0
        pos2 = len(s) - 1
        while pos1 < pos2:
            s[pos1], s[pos2] = s[pos2], s[pos1]
            pos1 += 1
            pos2 -= 1