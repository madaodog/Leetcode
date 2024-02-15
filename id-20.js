/**
 * 20. Valid Parentheses
 * Source: https://leetcode.com/problems/valid-parentheses/
 */


const closing_brackets = ['}', ')', ']']
const opposites = {
    '}' : '{',
    ')' : '(',
    ']' : '['
}

const isValid = (s) => {
    // LIFO
    stack = []

    for(let i = 0; i < s.length; i++) {
        if(closing_brackets.includes(s[i])) {
            if(stack[stack.length-1] === opposites[s[i]]) {
                stack.pop()
            } else {
                return false
            }
        } else {
            stack.push(s[i])
        }
    }
    const isEmpty = stack.length === 0 ? true : false
    return isEmpty
}

