/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBSTValue(root, Long.MIN_VALUE, Long.MAX_VALUE);
        
    }

    public boolean isValidBSTValue(TreeNode root, long mn, long mx) {
        if (root == null) return true;
        if (root.val <= mn || root.val >= mx) return false;
        
        return isValidBSTValue(root.left, mn, root.val) && isValidBSTValue(root.right, root.val, mx);
    }
}