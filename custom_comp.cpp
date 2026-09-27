
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool vect_comp1(const int &a, const int &b){
    if(a <= b){
        return false;
    }
    return true;
}

bool vect_comp2(const int &a, const int &b){
    if(a >= b){
        return true;
    }
    return false;
}

bool pairComp(const pair<int, int> &a, const pair<int, int> &b){
    if(a.first == b.first){
        if(a.second < b.second)
            return true;
        return false;
    }
    // a.first > b.first means they are in their correct order
    return a.first > b.first; 
}

int main() {
	// your code goes here
	
	vector<int> arr = {1,4,7,3,2,10,5};
    
    // sorting in asc order (by default) 	
    sort(arr.begin(), arr.end());
	for(auto i: arr){
	    cout << i << " ";
	}
	cout << endl;
	
	
    // sorting in desc order, there are many ways to do this
    // 1) vect_comp1
    // ----------------------------------------------------
	arr = {1,4,7,3,2,10,5};
    // sort will ask `comp(a, b)` are `a` & `b` in their desired order?
    // so you'll say if `a` <= `b` then `a` should come after `b`,
    // you'll return false to tell the sort they are not in correct order
    // and sort will swap a & b
    sort(arr.begin(), arr.end(), vect_comp1);
	for(auto i: arr){
	    cout << i << " ";
	}
	cout << endl;
	
    // 2) vect_comp2
    // ----------------------------------------------------
	arr = {1,4,7,3,2,10,5};
    // sort will ask `comp(a, b)` are `a` & `b` in their desired order?
    // so you'll say if `a` <= `b` then `a` should come before `b`,
    // you'll return `true` to tell the sort they are in correct order
    // and sort will not swap a & b
    sort(arr.begin(), arr.end(), vect_comp2);
	for(auto i: arr){
	    cout << i << " ";
	}
	cout << endl;	
	

    // sort the pair,
    // (pair a, pair b)
    // {{2,2}, {1,1}, {2,3}, {3,1}, {3,2}, {1,2}, {2,1}}
    // desired o/p : {{3,1}, {3,2}, {2,1}, {2,2}, {2,3}, {1,1}, {1, 2}}
	
	
	vector<pair<int, int>> PairARR = {{2,2}, {1,1}, {2,3}, {3,1}, {3,2}, {1,2}, {2,1}};
    sort(PairARR.begin(), PairARR.end(), pairComp);
	for(auto i: PairARR){
	    cout << "{" << i.first <<',' <<  i.second << "}, ";
	}
	cout << endl;	

}

