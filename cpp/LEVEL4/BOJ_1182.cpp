#include <iostream>
#include <vector>

using namespace std;

int cnt = 0;
int N, S;
vector<int> num(20);

void solution(int start, int sum) {
    if (sum == S && start != 0) {
        cnt ++;
    }

    for (int i = start; i < N; i++) {
        solution(i + 1, sum + num[i]);    
    }

    return;
}

int main() {
    cin >> N >> S;

    for (int i = 0; i < N; i++) {
        cin >> num[i];
    }

    solution(0, 0);

    cout << cnt;

    return 0;
}