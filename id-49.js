/**
 * 49. Group Anagrams
 * Source: https://leetcode.com/problems/group-anagrams/
 */


/**
 * Alternative solution would be to keep an array of size 26 for each word 
 * where each index represents the amount of occurences of the ith letter (eg counter[2] is the counter for the letter "c")
 * then group the words with wordA.count === wordB.count
 */

var groupAnagrams = (strs) => {
    hashMap = {};

    for(let i = 0; i < strs.length; i++) {
        sorted = strs[i].split("").sort().join("");
        if (sorted in hashMap) {
            hashMap[sorted].push(strs[i]);
        } else {
            hashMap[sorted] = [];
            hashMap[sorted].push(strs[i]);
        }
    }

    return Object.values(hashMap);
}




