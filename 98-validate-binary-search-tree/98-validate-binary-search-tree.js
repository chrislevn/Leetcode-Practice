/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    return helper(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
    
};

var helper = function(node, minValue, maxValue) {
    if (node == null) {
        return true;
    } 
    
    if (node.val > minValue && node.val < maxValue) {
        return (helper(node.left, minValue, node.val) && helper(node.right, node.val, maxValue));
    } else {
        return false;
    }
};