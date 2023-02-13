#include<iostream>
#include<cmath>

inline long long int fib(int n) {
    double phi = (1 + sqrt(5)) / 2;
    return round(pow(phi, n) / sqrt(5));
}

int main ()
{
    int n = 90;
    std::cout << fib(n) << std::endl;
    return 0;
}
