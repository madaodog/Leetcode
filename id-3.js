/**
 * 3. Longest Substring Without Repeating Characters
 * Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */

const lengthOfLongestSubstring = (s) => {
    const uniques = new Set()
    let maxLength = 0
    let left = 0

    for(let right = 0; right < s.length; right++) {
        while(uniques.has(s[right])) {
            uniques.delete(s[left])
            left++
        }
        uniques.add(s[right])
        maxLength = Math.max(maxLength, right - left + 1)
    }
    return maxLength
}