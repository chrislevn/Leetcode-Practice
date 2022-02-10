/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var chars = []
    var left = 0; 
    var right = 0; 
    var res = 0; 
    
    while (right < s.length) {
        const r = s[right]; 
        const index = chars[r]; 

        if (index != null && index >= left && index < right) {
            left = index + 1;  
        }
        res = Math.max(res, right - left + 1); 
        chars[r] = right; 
        right += 1;
    }
    return res;
};