'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
'''
def lengthOfLongestSubstring(s):
    fre_map=dict()
    low=0,high=0,res=0

    while high<len(s):
        fre_map[s[high]]=fre_map.get(s[high],0)+1

        while fre_map.get(s[high])>1:
            fre_map[s[low]]=fre_map.get(s[low])-1

            if fre_map.get(s[low])==0:
                del fre_map[s[low]]
            low+=1
        lenn=high-low+1
        res=max(res,lenn)
        high+=1

    return res