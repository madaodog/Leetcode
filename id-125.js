/**
 * 125. Valid Palindrome
 * Source: https://leetcode.com/problems/valid-palindrome/
 */

const isPalindrome = (s) => {
    const alphaNumeric = s.replace(/[^0-9A-Z]+/gi,"").toLowerCase();
    let l = 0
    let r = alphaNumeric.length - 1;
    if(alphaNumeric.length === 0) {
        return true;
    }

    while(l < r) {
        if(alphaNumeric[l] !== alphaNumeric[r]){
            console.log(alphaNumeric[l], alphaNumeric[r])
            return false; 
        }
        l++;
        r--;
    }
    return true;
}
