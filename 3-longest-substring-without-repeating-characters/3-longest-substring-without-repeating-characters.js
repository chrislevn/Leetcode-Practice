/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var k = 0;
    var maxLength = 0;
    for(i = 0; i < s.length; i++) {
        for (j = k; j < i; j++) {
            if (s[i] === s[j]) {
                k = j + 1;
                break;
            }
        }
        if (i - k + 1 > maxLength) {
            maxLength = i - k + 1;
        }
    }
    return maxLength;
}