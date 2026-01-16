#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 완전 탐색 구현
void dfs(int M, vector<int>& nums, int start, int cnt, vector<int>& answer) {
    if (cnt == M) {
        for (int a: answer) {
            cout << a << " ";   
        }
        cout << endl;
    } else {
        for (int i = start+1; i < nums.size(); i++) {
            answer.push_back(nums[i]);
            dfs(M, nums, i, cnt+1, answer);
            answer.pop_back();
        }
    }
}

void solution(int N, int M, vector<int>& nums) {
    sort(nums.begin(), nums.end()); // 사전순으로 정렬(오름차순)
    
    for (int i = 0; i < N; i++) {
        vector<int> answer; // 출력할 벡터
        int cnt = 1;
        answer.push_back(nums[i]);

        dfs(M, nums, i, cnt, answer);
    }
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> nums(N);

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }
    
    solution(N, M, nums);
    return 0;
}