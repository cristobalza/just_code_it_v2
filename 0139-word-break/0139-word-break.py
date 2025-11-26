class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i):

            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                if ((i + len(word)) <= len(s)) and (s[i: i + len(word)] == word):
                    memo[i] = dfs(i + len(word))
                    if memo[i]:
                        return True
        
            return False

        memo = {}
        return dfs(0)