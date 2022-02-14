/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
    var oddNumber = []; 
    var evenNumber = [];
    var result = [];
    
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] % 2 == 0) {
            evenNumber.push(nums[i]);
        } else {
            oddNumber.push(nums[i]);
        }
    };
    
    for (var i = 0; i < nums.length; i++) {
        if (i % 2 == 0) {
            result.push(evenNumber.pop());
        } else {
            result.push(oddNumber.pop())
        }
    }
    
    return result;
};