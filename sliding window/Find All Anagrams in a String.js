/**
 Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
 */

const findAnagrams = function (s, p) {
    let low = 0;
    let k = p.length;
    let high = k;
    let res = [];
    let sMap = new Map();
    let pMap = new Map();

    //add frequencies in pMap
    for (let i = 0; i < k; i++) {
        pMap.set(p[i], (pMap.get(p[i]) || 0) + 1);
    }
    let need = pMap.size;
    let have = 0;

    // add current window frequencies in sMap
    for (let i = 0; i < k; i++) {
        sMap.set(s[i], (sMap.get(s[i]) || 0) + 1);
    }
    //check if first window contains anagrams
    for (let [char, freq] of pMap) {
        if (sMap.get(char) === freq) have++;
    }

    if (need === have) res.push(low);

    for (high; high < s.length; high++) {
        //remove the low from sMap and also calculate have

        if (pMap.has(s[low])) {
            if (sMap.get(s[low]) === pMap.get(s[low])) have--;
            sMap.set(s[low], sMap.get(s[low]) - 1);
            if (sMap.get(s[low]) === pMap.get(s[low])) have++;
        }

        low++;

        // add high in sMap and also calculate have
        if (pMap.has(s[high])) {
            if (sMap.get(s[high]) === pMap.get(s[high])) have--;
            sMap.set(s[high], (sMap.get(s[high]) || 0) + 1);
            if (sMap.get(s[high]) === pMap.get(s[high])) have++;
        }

        if (have === need) res.push(low);
    }

    return res;
};
