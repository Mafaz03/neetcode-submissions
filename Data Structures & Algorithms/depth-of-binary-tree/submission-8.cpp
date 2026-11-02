/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    private:
        int dfs(TreeNode* node){

            if (node == nullptr){
                return 0;
            }


            int left = dfs(node->left);
            int right = dfs(node->right);

            if (left > right){
                return 1 + left;
            }
            else {
                return 1 + right;
            }

            
        }

    public:
        int maxDepth(TreeNode* root) {

            
            int res = dfs(root);
            return res;
            
        }
};
