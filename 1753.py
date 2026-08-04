s = input()
t = input()

M = 10**9 + 7
p = 31
q = 41

ps1 = [0] * (len(s) + 1)
ps2 = [0] * (len(s) + 1)

pw1 = 1
pw2 = 1
for i in range(len(s)):
    v = ord(s[i]) - ord("a")
    ps1[i] = (ps1[i - 1] + v * pw1) % M
    ps2[i] = (ps2[i - 1] + v * pw2) % M
    pw1 = (pw1 * p) % M
    pw2 = (pw2 * q) % M

h1, h2 = 0, 0
pw1, pw2 = 1, 1
for i in range(len(t)):
    v = ord(t[i]) - ord("a")
    h1 = (h1 + v * pw1) % M
    h2 = (h2 + v * pw2) % M
    pw1 = (pw1 * p) % M
    pw2 = (pw2 * q) % M

inv_pw = [1] * (len(s))
inv_qw = [1] * (len(s))
inv_p, inv_q = pow(p, -1, M), pow(q, -1, M)
for i in range(1, len(s)):
    inv_pw[i] = (inv_pw[i - 1] * inv_p) % M
    inv_qw[i] = (inv_qw[i - 1] * inv_q) % M

total = 0
for i in range(len(s) - len(t) + 1):
    v1 = ((ps1[i + len(t) - 1] - ps1[i - 1]) * inv_pw[i]) % M
    v2 = ((ps2[i + len(t) - 1] - ps2[i - 1]) * inv_qw[i]) % M
    if v1 == h1 and v2 == h2:
        total += 1

print(total)