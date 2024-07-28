import sys
    
input = sys.stdin.readline
N = int(input())
if (N * 15)%100 < 50:
    delete_student = int(N*0.15)
else:
    delete_student = int(N * 0.15 + 1)
std = []
solved_ac = 0

for i in range(1, N + 1):
    std.append(int(input()))
    
std.sort()
for i in range(N):
    if i + 1 > delete_student and N-i > delete_student:
        solved_ac += std[i]

if N == 0:
    print(0)
else:
    if ((solved_ac/(N-2*delete_student))*100)%100 < 50:
        print(int(solved_ac/(N-2*delete_student)))
    else:
        print(int(solved_ac/(N-2*delete_student)) + 1)