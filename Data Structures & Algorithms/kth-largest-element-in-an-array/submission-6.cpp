#include <queue>

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        priority_queue<int> heap;

        for (int n: nums){
            heap.push(n);
        }

        for (int i = 0; i < k-1; i++){
            heap.pop();
        }

        return heap.top();
        
    }
};
