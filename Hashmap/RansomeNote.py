'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

def ransomeNote(ransomeNote,magazine):
    if len(ransomeNote)>len(magazine):
        return False

    magMap=dict()
    ransomeMap=dict()
    for i in range(len(ransomeNote)):
        if not ransomeMap.get(ransomeNote[i]):
            ransomeMap[ransomeNote[i]]=1
        else:
            ransomeMap[ransomeNote[i]]= ransomeMap.get(ransomeNote[i])+1


    for i in range(len(magazine)):
        if not magMap.get(magazine[i]):
            magMap[magazine[i]]=1
        else:
            magMap[magazine[i]]=magMap.get(magazine[i])+1

    for key in ransomeMap:
        if not magMap.get(key):
            return False
        if magMap.get(key)<ransomeMap.get(key):
            return False

    return True