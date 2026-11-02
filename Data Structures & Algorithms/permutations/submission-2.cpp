class Solution {

    private:

        vector<vector<int>> results;
        void backtrack(int i, vector<int>& temp_res, vector<int>& nums, vector<bool> visited){

            if (temp_res.size() == nums.size()){
                results.push_back(temp_res);
                return;
            }

            for (int i = 0; i < nums.size(); i++){

                if (visited[i]){
                    continue;
                }

                temp_res.push_back(nums[i]);
                visited[i] = true;

                backtrack(i, temp_res, nums, visited);

                temp_res.pop_back();
                visited[i] = false;

            }
            
        
        }
        
    public:
        vector<vector<int>> permute(vector<int>& nums) {
            
            

            vector<int> temp_res;
            vector<bool> visited(nums.size(), false);

            
            backtrack(0, temp_res, nums, visited);

            return results;
        }
};
