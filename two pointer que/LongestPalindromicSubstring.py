'''
You're given a string s.

Find the longest contiguous substring of `s` that reads the same
forwards and backwards.

If more than one substring achieves the maximum length, return the one
that starts at the smallest index, so the result is always uniquely
determined.

Input: s = "babad"
Output: "bab"
"aba" is also a valid palindrome of length 3, but "bab" starts earlier (index 0 vs index 1), so it is returned
Input: s = "cbbd"
Output: "bb"
Input: s = "a"
Output: "a"
Constraints
1 <= s.length <= 1000
s consists of digits and English letters only
if multiple longest palindromic substrings exist, return the one starting at the smallest index
'''


def longestPenSubstring(s):
    def expand(left,right,s):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1

        return s[left+1:right]

    best=''
    for i in range(len(s)):
        odd=expand(i,i,s)

        if len(odd)>len(best):
            best=odd
        
        even=expand(i,i+1,s)

        if len(even)>len(best):
            best= even

    return best