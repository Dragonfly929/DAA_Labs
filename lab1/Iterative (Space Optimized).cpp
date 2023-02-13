// Fibonacci Series using Space Optimized Method
#include <iostream>
#include<bits/stdc++.h>

using namespace std;

inline long long int fib(int n) {
	long long int a = 0, b = 1, c;
	if(n == 0)
		return a;
	for (int i=2; i<=n; i++){
	c = a+b;
	a = b;
	b = c;
	}
	return b;
}

int main()
{
	int n = 90;
	cout << fib(n);
	return 0;
}
