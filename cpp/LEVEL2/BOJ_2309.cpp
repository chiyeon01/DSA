#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 최종 해결 함수
void solution(vector<int>& dwarf) {
    int tt = 0;
    int remove_one; // 제거할 하나의 난쟁이 인덱스
    int remove_two; // 제거할 또다른 난쟁이 인덱스
    bool IsFind = false; // 코드 기독성을 위해 발견하면 반복하지 않음

    for (int d: dwarf) {
        tt += d; // 전체 난쟁이(9명) 키의 합
    }

    for (int i = 0; i < 9; i++) {
        for (int j = i+1; j < 9; j++) {
            int sum = dwarf[i] + dwarf[j];
            if (tt - sum == 100) {
                remove_one = i;
                remove_two = j;
                IsFind = true;
                break;
            }
        }
        if (IsFind) {
            break;
        }
    }

    for (int i = 0; i < 9; i++) {
        if (i == remove_one || i == remove_two) { // 삭제 대상은 출력하지 않음
            continue;
        } else {
            cout << dwarf[i] << endl;
        }
    }
}

int main() {
    vector<int> dwarf(9);
    for (int i = 0; i < 9; i++) {
        cin >> dwarf[i];
    }

    // 오름차순으로 출력하기 위해 사전에 정렬
    sort(dwarf.begin(), dwarf.end());

    solution(dwarf);

    return 0;
}