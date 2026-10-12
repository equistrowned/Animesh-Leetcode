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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        printTree(root,res);
        return res;
    }

    public static void printTree(TreeNode root, List<Integer> nodes){
        if(root == null){
            return;
        }
        printTree(root.left,nodes);
        nodes.add(root.val);
        printTree(root.right,nodes);
    }
}