#include <iostream>
#include <vector>

using namespace std;

// 소수 구하기
bool is_prime_num(int num) {
    // 1 이하의 수는 예외처리
    if (num <= 1) {
        return false;
    }

    for (int i = 2; i < num; i++) {
        if (num % i == 0) { // 소수가 아닌 경우
            return false;
        }
    }

    return true;
}

int main() {
    int N;
    cin >> N;
    vector<int> nums(N);

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int answer = 0;
    for (int num: nums) {
        if (is_prime_num(num)) {
            answer ++;
        }
    }

    cout << answer;
    return 0;
}