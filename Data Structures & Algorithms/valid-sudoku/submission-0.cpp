#include <unordered_set>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // check each block
        for (int i = 0; i < 7; i+=3){
            for (int j = 0; j < 7; j+=3){
                
                unordered_set<char> seen;

                for (int idx_i = i; idx_i < i+3; idx_i++){
                    for (int idx_j = j; idx_j < j+3; idx_j++){

                        char t = board[idx_i][idx_j];

                        if (t != '.'){
                            if (seen.count(t)){
                                return false;
                            }
                            seen.insert(t);
                        }
                    }
                }
            }
            printf("\n");
        }

        // check each row
        for (int i = 0; i < 9; i ++){
            unordered_set<char> seen;

            for (int j = 0; j < 9; j++){
                
                char t = board[i][j];

                if (t != '.'){
                    if (seen.count(t)){
                        return false;
                    }
                    seen.insert(t);
                }
            }
        }

        // check each col
        for (int i = 0; i < 9; i ++){
            unordered_set<char> seen;

            for (int j = 0; j < 9; j++){
                
                char t = board[j][i];

                if (t != '.'){
                    if (seen.count(t)){
                        return false;
                    }
                    seen.insert(t);
                }
            }
        }

        return true;
    }

};
