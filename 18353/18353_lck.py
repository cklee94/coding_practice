import sys

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

dp = [1] * n

for i in range(1, len(data)):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
