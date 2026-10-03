'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

def longestPal(s):
    if len(s)==1:
        return 1

    mapp= dict()
    for i in range(len(s)):
        if not mapp.get(s[i]):
            mapp[s[i]]=1
        else:
            mapp[s[i]]= mapp.get([s[i]])+1

    res=0
    odd=False

    for key in mapp.keys():
        if mapp.get(key)%2==0:
            res+=mapp.get(key)
        else:
            odd=True

    if odd==False:
        return res

    for key in mapp.keys():
        if mapp.get(key)%2 ==1:
            res+= (mapp.get(key)-1)

    return res+1