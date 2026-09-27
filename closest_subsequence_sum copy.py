class Solution {
public:
    // Idea from:  https://www.youtube.com/watch?v=naz_9njI0I0
    // Meet in the middle
    // Divide array into 2 halves, and generate all the possible subset sum
    // if array has 6 elemene then, {1, 2, 3, ...}
    // first = 2^3 -> 8 subset sums  : {0, 1, 2, 3, 3, 4, 5, 6}
    // second = 2^3 -> 8 subset sums : {0, 11, 23, 34, 65, 15, 63, 9}
    // sort 2nd array and for each element in first, find the best complement (goal - s1) in 2nd sorted array

    // TC: 
    // 1. Divide half and generate subset sum --> 2*(2^(N/2)) 
    // 2. Sort 2^(N/2) element --> 2^(N/2)log(2^(N/2)) -->  N/2 * 2^(N/2)
    // 3. Iterate over 2^(N/2) elements (in first) and apply binary search on 2nd --> 2^(N/2) * N/2

    // let say n = 40, 2^(40/2) --> 2^20 * 20 + 2*2^20 --> 22 * (2*20) nearly 10^8


    vector<int> findAllSubsetSum(vector<int> nums, int start, int end, int offset){
        int n = end - start + 1;
        vector<int> subset_sums;
        for(int i = 0 ; i < (1 << n); i++){
            int summ = 0;
            for(int k = 0; k < n; k++){
                if(i &  1 << k){
                    summ += nums[k + offset];
                }
            }
            subset_sums.push_back(summ);
        }
        return subset_sums;
    }
    int minAbsDifference(vector<int>& nums, int goal) {
        int mid = nums.size()/2;
        int n = nums.size();
        if(n == 1) return abs(goal - nums[0]);

        vector<int> first = findAllSubsetSum(nums, 0, mid-1, 0);
        // for(int i = 0 ; i < first.size(); i++){
        //     cout << first[i] << " ";
        // }
        // cout << endl;

        vector<int> second = findAllSubsetSum(nums, mid, n-1, mid);
        sort(second.begin(), second.end());
        // for(int i = 0 ; i < second.size(); i++){
        //     cout << second[i] << " ";
        // }
        // cout << endl;

        int ans = 1e9;
        for(int i = 0; i < first.size(); i++){
            int s2 = goal - first[i];
            int ind = lower_bound(second.begin(), second.end(), s2) - second.begin();
            // if `ind` is out of bound then u have to take the last largest element
            if(ind >= second.size())
                ans = min(ans, abs(goal - first[i] - second[ind-1]));
            // if `ind` is within bound, then take `second[ind]`
            if(ind >= 0 && ind < second.size())
                ans = min(ans, abs(goal - first[i] - second[ind]));
        }
        return ans;
    }
};