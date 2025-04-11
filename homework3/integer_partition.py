import time


# 递归算法实现
def integer_partition(n, m):
    if n == 1 or m == 1:
        return 1
    elif n < m:
        return integer_partition(n, n)
    elif n == m:
        return 1 + integer_partition(n, n - 1)
    elif n > m > 1:
        return integer_partition(n - m, m) + integer_partition(n, m - 1)


# 动态规划实现
def integer_partition_dp(n, m):
    # 创建二维数组并初始化边界条件
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]
    return dp[n][m]


# 主函数
if __name__ == "__main__":
    for i in range(1,30):
        n = i
        m = i
        start_time = time.time()
        s1 = integer_partition(n, m)
        end_time = time.time()
        print(f"integer_partition({n}, {m})={s1}, {1000000 * (end_time - start_time)} μs")
        start_time = time.time()
        s2 = integer_partition_dp(n, m)
        end_time = time.time()
        print(f"integer_partition_dp({n}, {m})={s2}, {1000000 * (end_time - start_time)} μs")
