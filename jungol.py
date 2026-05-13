import sys
input = sys.stdin.readline

n, k1, k2 = map(int, input().split())
s_c_l = [list(map(int, input().split())) for _ in range(n)]
ans = [0 for _ in range(n)]

for i in range(n):
    arr = s_c_l.pop(0)
    x = n - i -1
    for j in range(x):
        k = abs(arr[0] - s_c_l[j][0])
        if arr[1] == s_c_l[j][1] and k <= k1:
            ans[i] += 1
            ans[j + n - x] += 1
        elif arr[1] != s_c_l[j][1] and k <= k2:
            ans[i] += 1
            ans[j + n - x] += 1

print(*ans)