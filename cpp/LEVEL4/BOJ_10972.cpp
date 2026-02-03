#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> arr;

void solution() {
    int start = N-1; // 내림차순 시작 부분
    int prev_num = arr[start]; // 내림차순의 마지막 숫자

    while (prev_num <= arr[start]) {
        if (start == 0) {
            start = -1;
            break;
        }

        prev_num = arr[start--];
    }
    
    if (start == -1) {
        cout << -1;
        return;
    }

    int tmp = 100000;
    int tmp_idx = 100000;
    
    for (int i = N-1; i > start; i--) {
        if (arr[i] > arr[start] && tmp > arr[i]) {
            tmp = arr[i];
            tmp_idx = i;
        }
    }

    // swap
    arr[tmp_idx] = arr[start];
    arr[start] = tmp;

    for (int i = start+1; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            if (arr[i] > arr[j]) {
                // swap
                int tp = arr[i];
                arr[i] = arr[j];
                arr[j] = tp;
            }
        }
    }

    for (int a: arr) {
        cout << a << " ";
    }

    return;
}

int main() {
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }

    solution();

    return 0;
}