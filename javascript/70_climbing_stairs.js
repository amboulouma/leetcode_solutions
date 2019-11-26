/**
 * @param {number} n
 * @return {number}
 * O(n) time
 * O(1) space
 * Dynamic approach  
 */
var climbStairs = function(n) {
    for(var i = 3, F = [0,1,2]; i <= n; i++) F[i] = F[i - 1] + F[i - 2];
    return F[n] || 1;
};
