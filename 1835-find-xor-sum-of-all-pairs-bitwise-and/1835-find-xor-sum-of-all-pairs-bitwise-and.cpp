class Solution {
public:
    int getXORSum(vector<int>& arr1, vector<int>& arr2) {
        int ans1 = 0; 
        int ans2 = 0; 
        for (auto const i:arr1) {
            ans1 ^= i;
        }
        for (auto const i:arr2) {
            ans2 ^= i;
        }
        
        return ans1&ans2;
    }
};