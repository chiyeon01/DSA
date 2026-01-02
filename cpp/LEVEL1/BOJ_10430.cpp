#include <iostream>

using namespace std;

void solution(int A, int B, int C) {
    int first_answer = (A+B)%C;
    int second_answer = (A*B)%C;
    cout << first_answer << endl;
    cout << first_answer << endl;
    cout << second_answer << endl;
    cout << second_answer << endl;
}

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    solution(A, B, C);
}