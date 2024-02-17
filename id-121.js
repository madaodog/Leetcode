/**
 * 121. Best Time to Buy and Sell Stock
 * Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 */


const maxProfit = (prices) => {
    left = 0
    right = 1
    profit = 0
    while(right <= prices.length) {
        if(prices[left] <= prices[right]) {
            profit = Math.max(profit, prices[right] - prices[left])
            right++
        } else {
            left = right
            right++
        }
    }
    return profit
}

console.log(maxProfit([7,1,5,3,6,4]))
