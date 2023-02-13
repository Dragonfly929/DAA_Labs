#include <iostream>
#include<bits/stdc++.h>

using namespace std;

inline long long int fib(int n) {
    if(n <= 1)
        return n;
    else return fib(n-1) + fib(n-2);
}

int main()
{
    int n = 90;
//    cin >> n;
    cout << fib(n) << endl;
    return 0;
}
