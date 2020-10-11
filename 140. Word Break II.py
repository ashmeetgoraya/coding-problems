'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.findSentence(s,wordDict,0,{}) if s else []

    def findSentence(self,s,wordDict,j,memo):
        if j in memo.keys(): return memo[j]

        sub = []
        for i in range(j,len(s)):
            if s[j:i+1] in wordDict:
                if i+1==len(s):
                    sub.append(s[j:])

                rest = self.findSentence(s,wordDict,i+1,memo)

                if rest:
                    for sent in rest:
                        sub.append(s[j:i+1]+" "+sent)
        memo[j] = sub
        return sub
