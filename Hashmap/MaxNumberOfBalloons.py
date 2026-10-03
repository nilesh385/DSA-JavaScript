'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.


Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
'''

def maxNumBalloons(text):
    if len(text)<7:
        return 0
    
    need={'a':1,'b':1,'l':2,'o':2,'n':1}
    have = dict()
    res=float('inf')

    for i in range(len(text)):
        if not have.get(text[i]):
            have[text[i]]=1
        else:
            have[text[i]]=have.get(text[i])+1

    for key in need.keys:
        if not have.get(key):
            return 0
        haveFre= have.get(key)
        needFre= need.get(key)
        times= haveFre/needFre
        res= min(res,times)

    return int(res)    