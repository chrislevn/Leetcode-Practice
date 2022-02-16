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
        let remain = prices[i] - prices[index];
        if (remain > 0) {
            result = Math.max(result, remain)
        } else {
            index = i;
        }
    }
    return result;
};