def climb(n):
    if n <= 2:
        return n

    a = [0] * (n + 1)
    a[1] = 1
    a[2] = 2

    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]

    return a[n]


def podotr(nums):
    m = i = nums[0]

    for num in nums[1:]:
        i = max(num, i + num)
        m = max(m, i)

    return m


def coins(n: int):
    coin = [1, 3, 4]
    m = 10**9
    a = [m] * (n + 1)
    a[0] = 0

    for s in range(1, n + 1):
        for c in coin:
            if s - c >= 0:
                a[s] = min(a[s], a[s - c] + 1)

    return a[n]


def levenshtein(a: str, b: str):
    n = len(a)
    m = len(b)


    a = [[0] * (m + 1) for _ in range(n + 1)]


    for i in range(n + 1):
        a[i][0] = i
    for j in range(m + 1):
        a[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            a[i][j] = min(
                a[i - 1][j] + 1,
                a[i][j - 1] + 1,
                a[i - 1][j - 1] + cost
            )

    return a[n][m]



