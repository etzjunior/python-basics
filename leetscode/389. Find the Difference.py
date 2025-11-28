class Solution(object):
    def findTheDifference(self, s, t):
        xor_value = 0
        for i in s + t:
            xor_value ^= ord(i)
        return chr(xor_value)