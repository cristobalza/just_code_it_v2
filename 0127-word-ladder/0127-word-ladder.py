class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        adj_list = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj_list[pattern].append(word)

        res = 1
        q = collections.deque([beginWord])
        visited = set([beginWord])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for j in range(len(node)):
                    pattern = node[:j] + "*" + node[j+1:]
                    for adj_word in adj_list[pattern]:
                        if adj_word not in visited:
                            visited.add(adj_word)
                            q.append(adj_word)

            res += 1

        return 0


