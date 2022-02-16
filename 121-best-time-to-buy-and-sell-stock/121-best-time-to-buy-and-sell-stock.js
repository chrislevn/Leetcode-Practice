/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length == 1) { 
        return 0;
    } 
    var index = 0; 
    var result = 0; 
    
    for (var i = 1; i < prices.length; i++) {
        if (prices[i] - prices[index] > 0) {
            result = Math.max(result, prices[i] - prices[index])
        } else {
            index = i;
        }
    }
    return result;
};