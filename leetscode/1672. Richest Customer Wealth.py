class Solution(object):
    def maximumWealth(self, accounts):
        adds = []
        for i in accounts:
            adds.append(sum(i))
        print(adds)
        wealth = max(adds)
        return wealth
