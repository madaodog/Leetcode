/**
 * 242. Valid Anagram
 * Source: https://leetcode.com/problems/valid-anagram/
 */

var isAnagram = function(s, t) {
    if(s.length !== t.length) {
        return false;
    }
    return s.split("").sort().join("") === t.split("").sort().join("");
};