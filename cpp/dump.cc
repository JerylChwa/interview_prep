#include <vector>
#include <iostream>
using namespace std;

class Solution{
public: 
    vector<int> resultArray(vector<int>& v) {
        int n = v.size();
        vector<int> ans;
        vector<int> v1, v2;
        v1.push_back(v[0]);
        v2.push_back(v[1]);

        for (int i = 2; i < v.size(); i++) {
            if (v1.back() > v2.back()) {
                v1.push_back(v[i]);
            } else {
                v2.push_back(v[i]);
            }
        }
        ans = v1;
        for (auto i : v2) {
            ans.push_back(i);
        }

        return ans;
    }
};



int main() {
    Solution s;
    vector<int> v = {};
    vector<int> res = s.resultArray(v);

    for (int x : res) cout << x << " ";
    
}