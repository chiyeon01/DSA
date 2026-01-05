#include <iostream>

using namespace std;

long long solution(int N) {
    long long result = 0;
    
    for (int i = 1; i < N + 1; i++) {
        result += (N / i) * i;
    }

    return result;
}

int main() {
    int N;
    cin >> N;
    long long answer = solution(N);
    cout << answer;
}