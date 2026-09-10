/*
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
*/

// approach 1 - optimized , not full optimized
const permutationString1 = function (s1, s2) {
    if (s1.length > s2.length) return false;

    let low = 0;
    let k = s1.length;
    let high = k - 1;
    let sMap = new Map();
    let windowMap = new Map();

    for (let i = 0; i < s1.length; i++) {
        sMap.set(s1[i], (sMap.get(s1[i]) || 0) + 1);
    }

    // Check whether first window satisfies requirements
    for (let [char, freq] of sMap) {
        if (windowMap.get(char) === freq) {
            have++;
        }
    }

    if (have === need) return true;

    for (let i = 0; i < k; i++) {
        windowMap.set(s2[i], (windowMap.get(s2[i]) || 0) + 1);
    }
    while (high < s2.length) {
        let same = true;
        for (let [char, freq] of sMap) {
            if (windowMap.get(char) !== freq) {
                same = false;
                break;
            }
        }
        if (same === true) return true;

        if (high + 1 >= s2.length) break;
        windowMap.set(s2[high + 1], (sMap.get(s1[high + 1]) || 0) + 1);
        windowMap.set(s2[low], sMap.get(s2[low]) - 1);
        high++;
        low++;
    }

    return false;
};

console.log(permutationString1("abc", "dfsafcba"));

const permustationString2 = function (s1, s2) {
    if (s1.length > s2.length) return false;

    let low = 0;
    let k = s1.length;
    let sMap = new Map();
    let windowMap = new Map();

    // add character & frequencies in sMap
    for (let i = 0; i < s1.length; i++) {
        sMap.set(s1[i], (sMap.get(s1[i]) || 0) + 1);
    }

    let need = sMap.size;
    let have = 0;

    //create first window map
    for (let i = 0; i < k; i++) {
        windowMap.set(s2[i], (windowMap.get(s2[i]) || 0) + 1);
    }

    // count have for first window map
    for (let [char, freq] of sMap) {
        if (windowMap.get(char) === freq) have++;
    }

    if (have === need) return true;

    for (let high = k; high < s2.length; high++) {
        //remove the character removing from the current window and also check for have
        if (sMap.has(s2[low])) {
            if (windowMap.get(s2[low]) === sMap.get(s2[low])) {
                have--;
            }

            windowMap.set(s2[low], windowMap.get(s2[low]) - 1);

            if (windowMap.get(s2[low]) === sMap.get(s2[low])) {
                have++;
            }
        }
        low++;

        //add the character in the current window and also check for have
        // windowMap.set(s2[high], (windowMap.get(s2[high]) || 0) + 1);
        if (sMap.has(s2[high])) {
            if (windowMap.get(s2[high]) === sMap.get(s2[high])) {
                have--;
            }

            windowMap.set(s2[high], (windowMap.get(s2[high]) || 0) + 1);
            if (windowMap.get(s2[high]) === sMap.get(s2[high])) {
                have++;
            }
        }

        if (need === have) return true;
    }
    return false;
};
