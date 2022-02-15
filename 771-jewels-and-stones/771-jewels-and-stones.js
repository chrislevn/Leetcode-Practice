/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    var jewel_dictionary = new Set(); 
    var result = 0;
    for (var i = 0; i < jewels.length; i++) {
        jewel_dictionary.add(jewels[i]);
    }
    
    for (var i = 0; i < stones.length; i++) {
        if (jewel_dictionary.has(stones[i])) {
            result++;
        }
    }
    return result;
};