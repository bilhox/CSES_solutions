from collections import defaultdict

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]
        self.rgraph = [[] for _ in range(2 * n)]
        self.comp = [-1] * (2 * n)
        self.nb_scc = 0
        self.solved = False
        self.satisfiable = None
        self.assignment = None

    def _node(self, var, value):
        return 2 * var + (0 if value else 1)

    def add_clause(self, a, va, b, vb):
        na = self._node(a, va)
        nb = self._node(b, vb)
        self.graph[na ^ 1].append(nb)
        self.graph[nb ^ 1].append(na)
        self.rgraph[nb].append(na ^ 1)
        self.rgraph[na].append(nb ^ 1)
        self.solved = False

    def add_implication(self, a, va, b, vb):
        self.add_clause(a, not va, b, vb)

    def force(self, a, va):
        self.add_clause(a, va, a, va)

    def _kosaraju(self):
        size = 2 * self.n
        visited = [False] * size
        order = []

        for start in range(size):
            if visited[start]:
                continue
            visited[start] = True
            stack = [(start, 0)]
            while stack:
                node, idx = stack.pop()
                if idx < len(self.graph[node]):
                    stack.append((node, idx + 1))
                    nxt = self.graph[node][idx]
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(node)

        self.comp = [-1] * size
        c = 0
        for start in reversed(order):
            if self.comp[start] != -1:
                continue
            self.comp[start] = c
            stack = [start]
            while stack:
                node = stack.pop()
                for nxt in self.rgraph[node]:
                    if self.comp[nxt] == -1:
                        self.comp[nxt] = c
                        stack.append(nxt)
            c += 1
        self.nb_scc = c

    def solve(self):
        self._kosaraju()
        self.satisfiable = True
        self.assignment = [False] * self.n
        for i in range(self.n):
            if self.comp[2 * i] == self.comp[2 * i + 1]:
                self.satisfiable = False
                self.assignment = None
                break
            self.assignment[i] = self.comp[2 * i] > self.comp[2 * i + 1]
        self.solved = True
        return self.satisfiable

    def is_satisfiable(self):
        if not self.solved:
            self.solve()
        return self.satisfiable

    def get_assignment(self):
        if not self.solved:
            self.solve()
        return self.assignment

    def get_scc_count(self):
        if not self.solved:
            self.solve()
        return self.nb_scc


n, m = map(int, input().split())
SAT = TwoSAT(m)
for _ in range(n):
    s1, a, s2, b = input().split()
    s1 = s1 == "+"
    s2 = s2 == "+"
    SAT.add_clause(int(a) - 1, s1, int(b) - 1, s2)

if not SAT.is_satisfiable():
    print("IMPOSSIBLE")
    exit()
print(*("-+"[v] for v in SAT.get_assignment()))