/**
 * 28. Find the Index of the First Occurrence in a String
 * Source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
 */

var strStr = (haystack, needle) => {
    if(needle.length > haystack.length) {
        return -1;
    } else {
            return strStrRecursive(haystack, needle, 0);
    }
}


var strStrRecursive = (haystack, needle, i) => {
    if(haystack.slice(i, i+needle.length) === needle) {
        return i;
    } else if(haystack.length-i > needle.length) {
        i++;
        return strStrRecursive(haystack, needle, i)
    } else {
        return -1;
    }
}