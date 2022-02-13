/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    var segmentCount = 0; 
    for (var i = 0; i < s.length; i++) {
        if ((i == 0 || s.charAt(i-1) == ' ') && s.charAt(i) != ' ') {
            segmentCount++;
        }
    }
    return segmentCount;
};