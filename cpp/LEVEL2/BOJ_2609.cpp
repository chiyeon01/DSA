#include <iostream>

using namespace std;

int GCD(int a, int b) {
    int range = min(a, b);
    int gcd = 1;

    for (int i = 1; i < range+1; i++) {
        if (a % i == 0 and b % i == 0) {
            gcd = i;
        }
    }

    return gcd;
}

int LCM(int a, int b) {
    int gcd = GCD(a, b);
    int lcm = (a / gcd) * (b / gcd) * gcd;
    
    
    return lcm;
}

int main() {
    int a,b;
    cin >> a >> b;
    
    int gcd = GCD(a, b);
    int lcm = LCM(a, b);

    cout << gcd << endl;
    cout << lcm << endl;

    return 0;
}