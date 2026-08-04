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

borders = []
for i in range(1, N):
    v1 = ((ps1[N - 1] - ps1[N - i - 1]) * inv_pw[N - i]) % M
    v2 = ((ps2[N - 1] - ps2[N - i - 1]) * inv_qw[N - i]) % M
    h1 = ps1[i - 1]
    h2 = ps2[i - 1]
    if v1 == h1 and v2 == h2:
        borders.append(i)

print(*borders)