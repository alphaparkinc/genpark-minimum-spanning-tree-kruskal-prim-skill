from typing import List, Tuple, Dict, Any

class MinimumSpanningTree:
    @staticmethod
    def kruskal(nodes: List[str], edges: List[Tuple[str, str, float]]) -> Dict[str, Any]:
        parent = {n: n for n in nodes}
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                return True
            return False
        sorted_edges = sorted(edges, key=lambda x: x[2])
        mst = []
        total_w = 0.0
        for u, v, w in sorted_edges:
            if union(u, v):
                mst.append({"from": u, "to": v, "weight": w})
                total_w += w
                if len(mst) == len(nodes) - 1:
                    break
        return {"mst_edges": mst, "total_weight": round(total_w, 2), "edge_count": len(mst)}

    def benchmark_mst(self) -> Dict[str, Any]:
        nodes = ["A", "B", "C", "D"]
        edges = [("A", "B", 1.0), ("B", "C", 2.0), ("A", "C", 3.0), ("C", "D", 1.0)]
        return self.kruskal(nodes, edges)
