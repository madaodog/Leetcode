/**
 * 875. Koko Eating Bananas
 * Source: https://leetcode.com/problems/koko-eating-bananas/
 */

const minEatingSpeed = (piles, h) => {
    left = 1
    right = Math.max(...piles)
    minimum = Math.max(...piles)
    while(left <= right) {
        mid = Math.floor((right + left)/2)
        hours = 0
        for(let i = 0; i < piles.length; i++) {
            hours += Math.ceil(piles[i] / mid)
        }
        if(hours <= h) {
            minimum = Math.min(minimum, mid)
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return minimum
}


