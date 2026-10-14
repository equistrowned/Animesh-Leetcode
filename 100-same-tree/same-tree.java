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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack <TreeNode> s1 = new Stack<>();
        Stack <TreeNode> s2 = new Stack<>();

        s1.push(p);
        s2.push(q);

        while(!s1.isEmpty() && !s2.isEmpty()){
            TreeNode a = s1.pop();
            TreeNode b = s2.pop();

            if(a == null && b ==null){
                continue;
            }

            if(a == null || b == null){
                return false;
            }

            if(a.val != b.val){
                return false;
            }

            s1.push(a.left);
            s1.push(a.right);

            s2.push(b.left);
            s2.push(b.right);


    }
            return s1.isEmpty() && s2.isEmpty();
        }

}