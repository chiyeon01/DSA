#include <iostream>
#include <vector>
#include <string>

using namespace std;

int N;
string s;
char board[10][10];
vector<int> sum(11, 0);
vector<int> answer;

// 현재 num_cnt가 가능한 수인지 확인하여 false or true를 반환하는 함수
bool IsPossible(int num_cnt) {

    for (int i = 0; i < num_cnt; i++) {
        // i - num_cnt-1(index)까지의 합이 조건과 다른 경우에는 false를 반환
        if (board[i][num_cnt-1] == '+' && sum[num_cnt] - sum[i] <= 0) return false;
        if (board[i][num_cnt-1] == '-' && sum[num_cnt] - sum[i] >= 0) return false; 
        if (board[i][num_cnt-1] == '0' && sum[num_cnt] - sum[i] != 0) return false;
    }

    // 모든 조건이 참인 경우, true 반환
    return true;
}

// solution
void solution(int num_cnt) {
    // num_cnt == N+1인 경우는 정답이 존재하는 경우
    if (num_cnt == N+1) {
        for (int a: answer) {
            cout << a << " ";
        }

        // 프로세스 종료
        exit(0);
    }
    
    // -10 ~ 10까지 탐색하며 가능한 경우를 찾음
    for (int i = -10; i <= 10; i++) {
        sum[num_cnt] = sum[num_cnt - 1] + i; // 누적합 알고리즘을 활용
        answer.push_back(i);

        if (IsPossible(num_cnt)) {
            solution(num_cnt+1); // 현재 값이 가능한 경우에 재귀
        }

        sum[num_cnt] = 0;
        answer.pop_back();
    }

    return;
}

int main() {
    cin >> N >> s;

    int idx = 0;

    for (int i = 0; i < N; i ++) {
        for (int j = i; j < N; j++) {
            board[i][j] = s[idx];
            idx++;
        }
    }

    solution(1);

    return 0;
}