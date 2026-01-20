#include <iostream>
#include <vector>
#include <string>

using namespace std;

int k;
vector<bool> IsUsed(10, false); // 해당 인덱스의 수가 사용됐는지 확인하는 변수
string minimum = "9999999999"; // 최소를 담는 변수
string maximum = "0"; // 최대를 담는 변수

void solution(string now_str, char prev, vector<char>& vec, int idx) {
    // 현재 str이 개수를 충족했을 때
    if (now_str.size() == k+1) {
        if (stoll(now_str) < stoll(minimum)) { // minimum 조건
            minimum = now_str;
        }
        if (stoll(now_str) > stoll(maximum)) { // maximum 조건
            maximum = now_str;
        }
        return;   
    } else if (idx == k){
        return;
    }
    
    int last_num = now_str[now_str.size()-1] - '0'; // 가장 마지막에 쓰인 숫자;

    if (prev == '>') {
        for (int i = 0; i < last_num; i++) {
            if (!IsUsed[i]) {
                IsUsed[i] = true;
                solution(now_str + to_string(i), vec[idx+1], vec, idx+1);
                IsUsed[i] = false;
            }
        }
    } else {
        for (int i = last_num+1; i < 10; i++) {
            if (!IsUsed[i]) {
                IsUsed[i] = true;
                solution(now_str + to_string(i), vec[idx+1], vec, idx+1);
                IsUsed[i] = false;
            }
        }
    }
}

int main() {
    cin >> k;
    vector<char> vec(k+1); // 부등호 넣을 벡터
    
    for (int i = 0; i < k; i++) {
        cin >> vec[i];
    }
    vec[k] = '>';

    for (int i = 0; i < 10; i++) {
        IsUsed[i] = true;
        solution(to_string(i), vec[0], vec, 0);
        IsUsed[i] = false;
    }

    cout << maximum << endl;
    cout << minimum << endl;

    return 0;
}