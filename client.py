from collections import deque

class HopcroftKarpMatcher:
    """Hopcroft-Karp O(E sqrt(V)) maximum bipartite matching."""
    def __init__(self, adj_u: dict[int, list[int]], u_size: int, v_size: int):
        self.adj = adj_u
        self.u_size = u_size
        self.v_size = v_size
        self.pair_u = {}
        self.pair_v = {}
        self.dist = {}

    def _bfs(self) -> bool:
        queue = deque()
        for u in range(self.u_size):
            if u not in self.pair_u:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        self.dist[None] = float('inf')

        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[None]:
                for v in self.adj.get(u, []):
                    next_u = self.pair_v.get(v, None)
                    if self.dist.get(next_u, float('inf')) == float('inf'):
                        self.dist[next_u] = self.dist[u] + 1
                        queue.append(next_u)
        return self.dist[None] != float('inf')

    def _dfs(self, u: int) -> bool:
        if u is not None:
            for v in self.adj.get(u, []):
                next_u = self.pair_v.get(v, None)
                if self.dist.get(next_u, float('inf')) == self.dist[u] + 1:
                    if self._dfs(next_u):
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True
            self.dist[u] = float('inf')
            return False
        return True

    def find_max_matching(self) -> dict:
        matching_size = 0
        while self._bfs():
            for u in range(self.u_size):
                if u not in self.pair_u:
                    if self._dfs(u):
                        matching_size += 1

        matches = [{"u": u, "v": v} for u, v in self.pair_u.items()]
        return {
            "max_matching_cardinality": matching_size,
            "matched_pairs": matches
        }
