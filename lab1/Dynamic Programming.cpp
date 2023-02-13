#include <iostream>
#include<bits/stdc++.h>

using namespace std;

inline long long int fib(int n) {
    int i;
    vector<long long int> v;
    v.push_back(0);
    v.push_back(1);
    for(i = 2; i <= n; i++)
        v.push_back(v[i-1] + v[i-2]);
    return v[n];
}

int main()
{
    int n = 90;
//    cin >> n;
    cout << fib(n) << endl;
    return 0;
}
