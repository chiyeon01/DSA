#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> factor) {
    sort(factor.begin(), factor.end());
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
    cout << answer;
}