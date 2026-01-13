#include <iostream>
#include <string>
#include <vector>

using namespace std;

int CanEatNum(int N, vector<string>& board) {
    int result = 0;
    char prev_color;

    for (int i = 0; i < N; i++) {
        int cnt = 0;
        string colors = board[i]; // 각 행
        prev_color = colors[0];

        // 행 탐색
        for (char color: colors) {
            if (prev_color == color) {
                cnt ++;
                result = max(result, cnt);
            } else {
                cnt = 1;
            }
            prev_color = color;
        }

        cnt = 0;
        prev_color = board[0][i];

        // 열 탐색
        for (int j = 0; j < N; j++) {
            if (prev_color == board[j][i]) {
                cnt ++;
                result = max(result, cnt);
            } else {
                cnt = 1;
            }
            prev_color = board[j][i];
        }
    }

    return result;
}

void solution(int N, vector<string>& board) {
    int answer = max(0, CanEatNum(N, board));
    char tmp;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            // 현재 색과 아래쪽 색을 바꾸기
            if (i < N-1) {
                tmp = board[i][j];
                board[i][j] = board[i+1][j];
                board[i+1][j] = tmp;

                answer = max(answer, CanEatNum(N, board));

                tmp = board[i][j];
                board[i][j] = board[i+1][j];
                board[i+1][j] = tmp;
            }

            // 현재 색과 오른쪽 색을 바꾸기
            if (j < N-1) {
                tmp = board[i][j];
                board[i][j] = board[i][j+1];
                board[i][j+1] = tmp;
                
                answer = max(answer, CanEatNum(N, board));

                tmp = board[i][j];
                board[i][j] = board[i][j+1];
                board[i][j+1] = tmp;
            }
        }
    }

    cout <<  answer;
}

int main() {
    int N;
    cin >> N;

    vector<string> board(N);
    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    solution(N, board);

    return 0;
}