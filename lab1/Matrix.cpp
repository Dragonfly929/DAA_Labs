#include<bits/stdc++.h>

#define lli unsigned long long int

using namespace std;

inline lli multiply(lli a[2][2], lli b[2][2]) {
    lli c,d,e,f;

    c=a[0][0]*b[0][0] + a[0][1]*b[1][0];
    d=a[0][0]*b[0][1] + a[0][1]*b[1][1];
    e=a[1][0]*b[0][0] + a[1][1]*b[1][0];
    f=a[1][0]*b[0][1] + a[1][1]*b[1][1];

    a[0][0]=c;
    a[0][1]=d;
    a[1][0]=e;
    a[1][1]=f;

}

inline lli power(lli a[2][2], int  n) {
    lli i;
    lli b[2][2] = {{1,1},{1,0}};
    for(i=2; i <= n; i++)
        multiply(a,b);

}

inline lli fib(int  n) {
    lli a[2][2] = {{1,1},{1,0}};
    if(n == 0)
        return 0;
    else {
        power(a, n-1);
        return a[0][0];
    }
}

int main()
{
    int  n=90;
    //cin >> n;
    cout << fib(n) << endl;
    return 0;
}

