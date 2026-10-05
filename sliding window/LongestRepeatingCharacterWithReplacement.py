'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

def charReplacement(s,k):
    low=0
    high=0
    res=0
    freq_map=dict()
    max_freq=0

    while high<len(s):
        # add the current char at high into the freq_map
        freq_map[s[high]]= freq_map.get(s[high],0)+1
        curWinLen= high-low+1 #current window length
        max_freq=max(max_freq,freq_map.get(s[high])) #check if the currently added char has higher frequency that max_freq or not and update it accordingly

        # if the difference between "current window length" subtracted by the element with max frequency is greater than k (number of replacements), then shrink the window (move left to the right side) to make it a valid window....
        while curWinLen-max_freq>k:
            freq_map[s[low]]-=1
            low+=1
            curWinLen=high-low+1 # again calculating the current window length because we are storing the value in a variable i.e. curWinLen

        high+=1
        res=max(curWinLen,res)
    return res