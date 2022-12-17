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
    int answer = 0;
    public int maxAncestorDiff(TreeNode root) {
        if (root == null){
            return 0;
        }
        dfs(root, root.val, root.val);
        return this.answer;
    }
    public void dfs(TreeNode root, int mn, int mx){
        if(root.val < mn) mn = root.val;
        if(root.val > mx) mx = root.val;
        if (this.answer < Math.abs(mx-mn)) this.answer = Math.abs(mx-mn);
        if(root.left != null) dfs(root.left, mn, mx);
        if(root.right != null) dfs(root.right, mn, mx);
    }
}