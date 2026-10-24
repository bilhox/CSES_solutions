s = input()
N = len(s)

M = 10**9 + 7
p = 31
q = 41

ps1 = [0] * (N + 1)
ps2 = [0] * (N + 1)

pw1 = 1
pw2 = 1
for i in range(N):
    v = ord(s[i]) - ord("a")
    ps1[i] = (ps1[i - 1] + v * pw1) % M
    ps2[i] = (ps2[i - 1] + v * pw2) % M
    pw1 = (pw1 * p) % M
    pw2 = (pw2 * q) % M

inv_pw = [1] * (N)
inv_qw = [1] * (N)
inv_p, inv_q = pow(p, -1, M), pow(q, -1, M)
for i in range(1, N):
    inv_pw[i] = (inv_pw[i - 1] * inv_p) % M
    inv_qw[i] = (inv_qw[i - 1] * inv_q) % M

periods = []
for k in range(1, N):
    period = None
    for i in range(0, N - N % k, k):
        v1 = ((ps1[i + k - 1] - ps1[i - 1]) * inv_pw[i]) % M
        v2 = ((ps2[i + k - 1] - ps2[i - 1]) * inv_qw[i]) % M
        if period is None:
            period = (v1, v2)
        elif (v1, v2) != period:
            break
    else:
        if N % k == 0:
            periods.append(k)
            continue
        rem = N % k
        v1 = ((ps1[N - 1] - ps1[N - rem - 1]) * inv_pw[N - rem]) % M
        v2 = ((ps2[N - 1] - ps2[N - rem - 1]) * inv_qw[N - rem]) % M
        h1 = ps1[rem - 1]
        h2 = ps2[rem - 1]
        if v1 == h1 and v2 == h2:
            periods.append(k)
periods.append(N)
print(*periods)