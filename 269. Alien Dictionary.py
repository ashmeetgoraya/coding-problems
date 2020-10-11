"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters, graph, in_degree = set(), defaultdict(list), defaultdict(int)

        for wrd in words:
            for char in wrd:
                letters.add(char)

        for i in range(1,len(words)):
            m, n = len(words[i-1]), len(words[i])
            j, uppr_lim = 0, min(m,n)

            while j < uppr_lim and words[i-1][j] == words[i][j]:
                j += 1

            if j == n and m > n:
                return ""

            if j < uppr_lim:
                graph[words[i-1][j]].append(words[i][j])
                in_degree[words[i][j]] += 1

        res, L = [], deque([x for x in letters if not in_degree[x]])
        while L:
            node = L.popleft()

            res.append(node)

            for nei in graph[node]:
                in_degree[nei] -= 1

                if not in_degree[nei]:
                    L.append(nei)

        return "".join(res) if not any(in_degree.values()) else ""
