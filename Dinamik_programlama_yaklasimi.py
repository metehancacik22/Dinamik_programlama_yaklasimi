def minimize_total_time(processing_time, transition_cost):
    n = len(processing_time)  # İş sayısı
    m = len(processing_time[0])  # Makine sayısı

    # DP tablosu: dp[i][j] = i. işi j. makinede bitirmenin minimum süresi
    dp = [[float('inf')] * m for _ in range(n)]

    # İlk iş için sadece işlenme süresi
    for j in range(m):
        dp[0][j] = processing_time[0][j]

    # Diğer işler için
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + transition_cost[k][j] + processing_time[i][j])

    # Son işten minimumu bul
    return min(dp[n - 1])


# TEST
processing_time = [
    [4, 6],  # İş 1 için M1: 4, M2: 6
    [7, 8],  # İş 2 için M1: 7, M2: 8
    [5, 6]  # İş 3 için M1: 5, M2: 6
]

transition_cost = [
    [0, 2],  # M1 -> M1:0, M1 -> M2:2
    [2, 0]  # M2 -> M1:2, M2 -> M2:0
]

print(minimize_total_time(processing_time, transition_cost))
