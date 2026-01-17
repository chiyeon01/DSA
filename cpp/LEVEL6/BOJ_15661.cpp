#include <iostream>
#include <vector>

using namespace std;

int diff(int a, int b) {
    if (a > b) {
        return a - b;
    } else {
        return b - a;
    }
}

void dfs(int N, int start, int team1, int team2, int& answer, int cnt, vector<vector<int>>& S, vector<bool>& IsTeam1, vector<bool>& IsTeam2) {
    if (cnt == N) {
        return;
    }

    answer = min(answer, diff(team1, team2));

    for (int i = start+1; i < N; i++) {
        team1 = 0;
        team2 = 0;
        IsTeam1[i] = false;
        IsTeam2[i] = true;

        for (int j = 0; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                if (IsTeam1[j] && IsTeam1[k]) {
                    team1 += S[j][k];
                    team1 += S[k][j];
                }
                if (IsTeam2[j] && IsTeam2[k]) {
                    team2 += S[j][k];
                    team2 += S[k][j];
                }
            }
        }
        
        dfs(N, i, team1, team2, answer, cnt+1, S, IsTeam1, IsTeam2);

        IsTeam1[i] = true;
        IsTeam2[i] = false;
    }
}

int solution(int N, vector<vector<int>>& S, vector<bool> IsTeam1, vector<bool> IsTeam2) {
    int team1 = 0;
    int team2 = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            team1 += S[i][j];
        }
    }

    int answer = team1; // 가장 큰 차이인 경우

    for (int i = 0; i < N; i++) {
        team1 = 0;
        team2 = 0;
        IsTeam1[i] = false;
        IsTeam2[i] = true;

        for (int j = 0; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                if (IsTeam1[j] && IsTeam1[k]) {
                    team1 += S[j][k];
                    team1 += S[k][j];
                }
                if (IsTeam2[j] && IsTeam2[k]) {
                    team2 += S[j][k];
                    team2 += S[k][j];
                }
            }
        }

        dfs(N, i, team1, team2, answer, 1, S, IsTeam1, IsTeam2);

        IsTeam1[i] = true;
        IsTeam2[i] = false;

    }

    return answer;
}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> S(N, vector<int>(N));
    vector<bool> IsTeam1(N, true);
    vector<bool> IsTeam2(N, false);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> S[i][j];
        }
    }

    int answer = solution(N, S, IsTeam1, IsTeam2);

    cout << answer;

    return 0;
}