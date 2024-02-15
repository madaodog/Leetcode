/**
 * 150. Evaluate Reverse Polish Notation
 * Source: https://leetcode.com/problems/evaluate-reverse-polish-notation
 */

const evalRPN = (tokens) => {
    const stack = []
    for(let i = 0; i < tokens.length; i++) {
        if(!isNaN(tokens[i])) {
            stack.push(parseInt(tokens[i]))
        } else {
            const secondNumber = stack.pop()
            const firstNumber = stack.pop()
            switch (tokens[i]) {
                case '*':
                    stack.push(firstNumber * secondNumber)
                    break;
                case '+':
                    stack.push(firstNumber + secondNumber)
                    break;
                case '/':
                    stack.push(parseInt(firstNumber / secondNumber))
                    break;
                case '-':
                    stack.push(firstNumber - secondNumber)
                    break;
            } }
    }
    return stack.pop()
}
