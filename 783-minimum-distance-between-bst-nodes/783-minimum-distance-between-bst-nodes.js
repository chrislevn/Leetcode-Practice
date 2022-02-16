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
 * @return {number}
 */
var minDiffInBST = function(root) {
    var prev; 
    var ans; 
    ans = Number.MAX_VALUE;
    var dfs = function(node) {
        if (node == null) {
            return;
        }
        dfs(node.left); 
        if (prev != null) {
            ans = Math.min(ans, node.val - prev);
        }
    prev = node.val;
    dfs(node.right);
}
    
    dfs(root); 
    return ans;  
};

