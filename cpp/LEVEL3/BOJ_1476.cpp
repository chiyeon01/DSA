#include <iostream>

using namespace std;

int solution(int E, int S, int M) {
    int answer = 1;
    int e = 1, s = 1, m = 1;

    while (true) {
        if (E == e && S == s && M == m) {
            break;
        }

        e = max(1, (e + 1) % 16);
        s = max(1, (s + 1) % 29);
        m = max(1, (m + 1) % 20);
        
        answer++;
    }

    return answer;
}

int main() {
    int E, S, M;
    cin >> E >> S >> M;

    int answer = solution(E, S, M);

    cout << answer;

    return 0;
}