class TwoSat:

    def __init__(self, n):
        self.n = n
        self._answer = [False] * n
        self.graph = [[] for _ in range(2 * n)]

    def add_clause(self, i, f, j, g):
        self.graph[2 * i + (0 if f else 1)].append(2 * j + (1 if g else 0))
        self.graph[2 * j + (0 if g else 1)].append(2 * i + (1 if f else 0))

    def satisfiable(self):
        n2 = 2 * self.n
        order = []
        visited = [False] * n2

        def dfs1(u):
            visited[u] = True
            for v in self.graph[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)

        for i in range(n2):
            if not visited[i]:
                dfs1(i)

        rev_graph = [[] for _ in range(n2)]
        for u in range(n2):
            for v in self.graph[u]:
                rev_graph[v].append(u)

        comp = [-1] * n2
        label = 0

        def dfs2(u, l):
            comp[u] = l
            for v in rev_graph[u]:
                if comp[v] == -1:
                    dfs2(v, l)

        for u in reversed(order):
            if comp[u] == -1:
                dfs2(u, label)
                label += 1

        for i in range(self.n):
            if comp[2 * i] == comp[2 * i + 1]:
                return False
        self._answer[i] = comp[2 * i] > comp[2 * i + 1]
        return True

    def answer(self):
        return self._answer