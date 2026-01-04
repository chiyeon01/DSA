#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> factor) {
    // 진짜 약수를 오름차순 정렬
    sort(factor.begin(), factor.end());
    // 가장 작은 값과 가장 큰 값을 곱하여 N 도출
    return factor[0] * factor[factor.size()-1];
}

int main() {
    int N;
    cin >> N;
    vector<int> factor(N);
    
    for (int i = 0; i < N; i++) {
        cin >> factor[i];
    }

    int answer = solution(factor);
    cout << answer; // 정답
}