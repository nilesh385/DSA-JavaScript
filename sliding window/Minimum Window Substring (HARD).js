/*
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
*/

const minWindow = function (s, t) {
    if (s.length < t.length) return "";

    let low = 0;
    let res = Infinity;
    let startIndex = 0;
    let sMap = new Map();
    let tMap = new Map();
    let need = 0;
    let have = 0;
    for (let i = 0; i < t.length; i++) {
        tMap.set(t[i], (tMap.get(t[i]) || 0) + 1);
    }
    need = tMap.size;
    for (let high = 0; high < s.length; high++) {
        sMap.set(s[high], (sMap.get(s[high]) || 0) + 1);

        if (tMap.has(s[high]) && sMap.get(s[high]) === tMap.get(s[high])) {
            have++;

            while (have === need) {
                let len = high - low + 1;
                if (len < res) {
                    res = len;
                    startIndex = low;
                }

                if (tMap.has(s[low]) && sMap.get(s[low]) === tMap.get(s[low]))
                    have--;

                sMap.set(s[low], sMap.get(s[low]) - 1);
                low++;
            }
        }
    }

    return res === Infinity ? "" : s.substring(startIndex, startIndex + res);
};

console.log(minWindow("ADOBECODEBANC", "ABC"));
