'''
You're given a string made up of words separated by one or more spaces,
and possibly with leading or trailing spaces too. A "word" is a maximal
run of non-space characters.

Return the length of the last word in the string.

The string always contains at least one non-space character, so there
is always a last word to find.

Input: s = "Hello World"
Output: 5
the last word is "World", which has 5 characters
Input: s = " fly me to the moon "
Output: 4
trailing spaces are ignored; the last word is "moon"
Input: s = "luffy is still joyboy"
Output: 6
the last word is "joyboy"
Constraints
1 <= s.length <= 10^4
s consists of English letters and spaces only
there is at least one word in s
'''

def lengthOfLastWord(s):
        s=s.rstrip()
        right=len(s)-1
        if len(s)==1:
            return 1

        while(right>=0):
            if s[right]==' ':
                return (len(s)-right)-1
            elif right==0:
                 return len(s)
            else :
                right-=1

s = "Programming"
# s = " fly me to the moon "
print(len(s))
print(   lengthOfLastWord(s))