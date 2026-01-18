class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)  # O(1) lookup
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        # Optional optimization: no need to check word lengths bigger than max word
        max_len = max((len(w) for w in word_set), default=0)

        for i in range(1, n + 1):
            # only look back up to max_len
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
