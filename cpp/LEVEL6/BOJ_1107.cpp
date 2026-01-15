#include <iostream>
#include <vector>

using namespace std;

// 두 수의 절댓값 차이를 찾아주는 함수
int diff(int a, int b) {
    if (a < b) {
        return b - a;
    } else {
        return a - b;
    }
}

// 최종 solution
int solution(int N, int M, vector<bool>& broken_button) {
    // 처음 answer값은 현재 채널과의 차이로 나타낼 수 있음.
    int answer = diff(N, 100);

    // i를 최대 범위까지 확장해서 완전 탐색
    for (int i = 0; i < 1000001; i++) {
        bool can_change = true;
        int tmp = i;
        int digit = 0;

        // 0 채널의 경우 예외로 처리해야함
        if (i == 0) {
            if (!broken_button[i]) {
                answer = min(answer, diff(N, i) + 1);
                continue;
            }
            continue;
        }

        while (tmp != 0) {
            int button = tmp % 10;
            
            if (broken_button[button]) {
                can_change = false;        
                break;
            }
            tmp /= 10;
            digit ++; // 자리수
        }

        if (can_change) {
            // 채널 입력하는 digit과 이동 후 채널 i와 N의 차이를 더함
            answer = min(answer, diff(N, i) + digit);
        }
    }

    return answer;
}

int main() {
    int N, M;
    vector<bool> broken_button(10, false);
    int answer;
    cin >> N;
    cin >> M;

    
    for (int i = 0; i < M; i++) {
        int button;
        cin >> button;
        broken_button[button] = true; // 부서진 버튼만 따로 기억
    }

    answer = solution(N, M, broken_button);
    
    cout << answer;

    return 0;
}