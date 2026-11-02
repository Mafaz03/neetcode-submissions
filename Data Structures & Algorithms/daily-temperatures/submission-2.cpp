#include <vector>
#include <stack>

class Solution {
    public:
        vector<int> dailyTemperatures(vector<int>& temperatures) {
            vector<int> result;
            for (int i = 0; i < temperatures.size(); i++){
                result.push_back(0);
            }
            
            stack<vector<int>> s;

            for (int ele = 0; ele < temperatures.size(); ele ++){

                while (!s.empty() && s.top()[0] < temperatures[ele]){
                    vector<int> temp = s.top();
                    s.pop();
                    int value = temp[0];
                    int idx = temp[1];

                    int gap = ele - idx;
                    result[idx] = gap;
                    
                }
                vector<int> temp = {temperatures[ele], ele};
                s.push(temp);

            }

            return result;

        }
};
