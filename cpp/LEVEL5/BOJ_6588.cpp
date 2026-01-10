#include <iostream>
#include <vector>

using namespace std;

// 소수를 벡터에 저장
void make_prime_number(vector<bool>& is_prime_number, vector<int>& prime_numbers) {
    is_prime_number[0] = false;
    is_prime_number[1] = false;
    for (int i = 2; i < 1001; i++) {
        for (int j = i*2; j < 1000001; j+=i) {
            is_prime_number[j] = false;
        }
    }

    for (int i = 3; i < 1000001; i++) {
        if (is_prime_number[i]) {
            prime_numbers.push_back(i);
        }
    }
}

void solution(vector<bool>& is_prime_number, vector<int>& prime_numbers, int n) {
    for (int prime_number: prime_numbers) {
        if (prime_number >= n) {
            printf("Goldbach's conjecture is wrong.\n");
            break;
        } else if (is_prime_number[n-prime_number]) {
            printf("%d = %d + %d\n", n, prime_number, n-prime_number);
            break;
        }
    }
}

int main() {
    vector<bool> is_prime_number(1000001, true);
    vector<int> prime_numbers;
    make_prime_number(is_prime_number, prime_numbers); // is_prime_number와 prime_numbers 채우기

    while (true) {
        int n;
        scanf("%d", &n);

        if (n == 0) {
            break;
        }

        solution(is_prime_number, prime_numbers, n);
    }
    return 0;
}