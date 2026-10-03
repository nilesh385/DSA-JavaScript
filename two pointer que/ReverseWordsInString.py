'''
You're given a string s that may contain leading spaces, trailing
spaces, and multiple spaces between words.

Return a new string with the words in reverse order, separated by exactly one space each, with no leading or trailing spaces.

A word is defined as a maximal run of non-space characters.

Input: s = "the sky is blue"
Output: "blue is sky the"
Input: s = " hello world "
Output: "world hello"
leading and trailing spaces are removed from the result
Input: s = "a good example"
Output: "example good a"
multiple spaces between words in the input collapse to a single space in the output
Constraints
1 <= s.length <= 10^4
s consists of English letters, digits, and spaces ' '
there is at least one word in s
'''

def reverseWords(s):
    res=[]
    right= len(s)-1

    while right>=0:
        while right>=0 and s[right]==' ':
            right-=1
        if right <0:
            break
        left=right

        while left>=0 and s[left]!=' ':
            left-=1

        res.append(s[left+1:right+1])
        right=left
        
    return " ".join(res)

s = "the sky is blue"
print(reverseWords(s))