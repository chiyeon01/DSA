#include <iostream>
#include <vector>

using namespace std;

void solution(int N, int M) {
    vector<bool> prime_number(1000001, true);
    prime_number[1] = false;
    prime_number[0] = false;

    for (int i = 2; i < 1001; i++) {
        for (int j = 2*i; j < 1000001; j+=i) {
            prime_number[j] = false;
        }
    }

    for (int i = N; i < M+1; i++) {
        if (prime_number[i]) {
            printf("%d\n", i);
        }
    }
}

int main() {
    int N, M;
    cin >> N >> M;
    solution(N, M);
    return 0;
}