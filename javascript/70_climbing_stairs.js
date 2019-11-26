/**
 * @param {number} n
 * @return {number}
 * O(n) time
 * O(n) space
 * Dynamic approach  
 */
var climbStairs = function(n) {
    for(var i = 3, F = [0,1,2]; i <= n; i++) F[i] = F[i - 1] + F[i - 2];
    return F[n] || 1;
};

/**
 * @param {number} n
 * @return {number}
 * O(n) Time
 * O(1) Space
 * Dynamic Approach
 */
var climbStairs1 = function(n) {
    let a = 1, b = 2, next;
    for(let i = 3; i <= n; i++) {
        next = a + b;
        a = b;
        b = next;
    }
    return n === 1 ? a : b;
};