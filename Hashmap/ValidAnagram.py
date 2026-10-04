'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

def validAnagram(s,t):
    if len(s) != len(t):
        return False
        
    sMap=dict()
    tMap=dict()

    for i in range(len(s)):
        if not sMap.get(s[i]):
            sMap[s[i]]=1
        else:
            sMap[s[i]]=sMap.get(s[i])+1

    for i in range(len(t)):
        if not tMap.get(t[i]):
            tMap[t[i]]=1
        else:
            tMap[t[i]]=tMap.get(t[i])+1

    for key in sMap.keys():
        if sMap.get(key)!=tMap.get(key):
            return False

    return True