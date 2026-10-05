'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s2)<len(s1):
#             return False
        
#         low=0
#         high=len(s1)-1
#         need_map=dict()
#         have_map=dict()

#         for i in range(len(s1)):
#             need_map[s1[i]]=need_map.get(s1[i],0)+1
        
#         need= len(need_map)
#         have=0

#         for i in range(len(s1)):
#             have_map[s2[i]]= have_map.get(s2[i],0)+1

#         for key in have_map.keys():
#             if need_map.get(key,0) == have_map.get(key):
#                 have+=1
        
#         if need==have:
#             return True

#         while high+1<len(s2):
#             if need_map.get(s2[low]):
#                 if need_map.get(s2[low])==have_map.get(s2[low]):
#                     have-=1
#                 #reduce frequence of low element
#                 have_map[s2[low]]=have_map.get(s2[low])-1
#                 if need_map.get(s2[low])==have_map.get(s2[low]):
#                     have+=1
#             low+=1
#             high+=1
#             if need_map.get(s2[high]):
#                 if need_map.get(s2[high])==have_map.get(s2[high]):
#                     have-=1
#                 #reduce frequence of high element
#                 have_map[s2[high]]=have_map.get(s2[high])+1
#                 if need_map.get(s2[high])==have_map.get(s2[high]):
#                     have+=1
            
#             if need==have:
#                 return True                

#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        for ch in s2[:len(s1)]:
            window[ch] = window.get(ch, 0) + 1

        if need == window:
            return True

        for i in range(len(s1), len(s2)):

            # Add new character
            window[s2[i]] = window.get(s2[i], 0) + 1

            # Remove old character
            left = s2[i - len(s1)]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if need == window:
                return True

        return False