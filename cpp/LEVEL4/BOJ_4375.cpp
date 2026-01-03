#include <iostream>

using namespace std;

void solution(int n) {
    long long start = 1;
    int answer = 1;

    // 나누어 떨어질 때까지
    while (start % n != 0) {
        // start는 prev_start를 모듈러 연산한 것에 기반
        start = (start % n) * 10 + 1;
        // 현재 자리수 계산
        answer ++;
    }

    cout << answer << endl;
}

int main() {
    int n;
    while (true) {
        cin >> n;
        if (cin.eof()) break;
        solution(n);
    }

    return 0;
}
