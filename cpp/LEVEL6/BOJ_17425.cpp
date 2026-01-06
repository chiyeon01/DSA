#include <iostream>
#include <vector>

using namespace std;

void solution(int N, vector<long>& f, vector<long>& g) {
    for (int i = 1; i < N + 1; i++) {
        for (int j = i; j < N + 1; j+=i) {
            f[j] += i;
        }
        g[i] = g[i-1] + f[i];
    }
}

int main() {
    vector<long> f(1000001);
    vector<long> g(1000001);

    solution(1000001, f, g);

    int T, N;
    cin >> T;
    for (int i = 0; i < T; i++) {
        scanf("%d", &N);
        printf("%ld\n", g[N]);
    }
}