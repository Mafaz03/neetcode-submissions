#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
private:
    map<vector<int>, int> dp;

    int backtrack(vector<int> &prices, int i, bool buy){
        // FIX 1: Use >= to prevent out-of-bounds access
        if (i >= prices.size()){
            return 0;
        }

        vector<int> key = {i, buy};
        if (dp.count(key)){
            return dp[key];
        }
        
        int profit = 0;
        if (buy){
            int buying   = backtrack(prices, i + 1, false) - prices[i]; // Buy
            int cooldown = backtrack(prices, i + 1, true);              // Cooldown
            profit = max(buying, cooldown);
        }
        else {
            int selling  = backtrack(prices, i + 2, true) + prices[i]; // Sell (skip 1 day -> i + 2)
            // FIX 2: Keep buy as false because we are still holding the stock
            int cooldown = backtrack(prices, i + 1, false);              // Hold
            profit = max(selling, cooldown);
        }

        return dp[key] = profit;
    }

public:
    int maxProfit(vector<int>& prices) {
        dp.clear();
        return backtrack(prices, 0, true);
    }
};