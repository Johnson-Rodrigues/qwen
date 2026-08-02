#!/usr/bin/env python3
"""
Solution for Modular Path Sum problem.

Key insight: For a path between u and v with LCA = w, the sum is:
S(u, v) = D[u] + D[v] - D[w] - D[parent[w]] (if parent exists) - but simpler:
S(u, v) = D[u] + D[v] - 2*D[w] + a[w]

where D[u] is the prefix sum from root to u (inclusive).

We use centroid decomposition to count pairs efficiently:
- For each centroid, we count paths passing through it
- We track prefix sums modulo k from the centroid
- For two nodes in different subtrees of the centroid, their path goes through the centroid
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input_data[idx]) % k
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Centroid decomposition
    sz = [0] * (n + 1)
    removed = [False] * (n + 1)
    
    def calc_size(u, p):
        sz[u] = 1
        for v in adj[u]:
            if v != p and not removed[v]:
                calc_size(v, u)
                sz[u] += sz[v]
    
    def find_centroid(u, p, total):
        for v in adj[u]:
            if v != p and not removed[v] and sz[v] > total // 2:
                return find_centroid(v, u, total)
        return u
    
    # D[u] = prefix sum from root (vertex 1) to u
    # But for centroid decomposition, we need to compute sums differently
    
    # Actually, let's use a different approach:
    # Root the tree at vertex 1, compute D[u] for all u
    # Then use centroid decomposition where for each centroid c,
    # we look at paths going through c
    
    # Recompute: D[u] = sum of a values from root to u (inclusive)
    D = [0] * (n + 1)
    parent = [0] * (n + 1)
    
    def dfs_prefix(u, p, cur_sum):
        D[u] = (cur_sum + a[u]) % k
        parent[u] = p
        for v in adj[u]:
            if v != p:
                dfs_prefix(v, u, D[u])
    
    dfs_prefix(1, 0, 0)
    
    answer = 0
    
    # For centroid decomposition, we need to count paths through each centroid
    # A path (u, v) goes through centroid c if u and v are in different subtrees of c
    # (or one of them is c itself)
    
    # For such a path: S(u, v) = D[u] + D[v] - 2*D[c] + a[c] (mod k)
    # We want S(u, v) ≡ 0 (mod k)
    # So: D[u] + D[v] - 2*D[c] + a[c] ≡ 0 (mod k)
    # => D[u] + D[v] ≡ 2*D[c] - a[c] (mod k)
    
    def count_paths_through_centroid(c):
        nonlocal answer
        
        # Collect all nodes in each subtree of c (in the original tree structure, considering removed nodes)
        # and compute their D values
        
        # For the centroid itself as one endpoint:
        # S(c, v) = D[c] + D[v] - D[c] = D[v] (if c is ancestor of v)
        # Wait, that's not right either. Let me reconsider.
        
        # Actually for centroid decomposition, we should think differently.
        # When c is the centroid, we consider all paths that pass through c.
        # For such a path (u, v), c lies on the path between u and v.
        
        # In the original rooted tree (rooted at 1), the relationship is complex.
        # Let's instead compute distances from the centroid within the current component.
        
        # Let dist_c[u] = sum of a values on path from c to u (including both)
        # For two nodes u, v in different subtrees of c, the path between them
        # goes through c, so S(u, v) = dist_c[u] + dist_c[v] - a[c]
        
        # We want: dist_c[u] + dist_c[v] - a[c] ≡ 0 (mod k)
        # => dist_c[u] + dist_c[v] ≡ a[c] (mod k)
        
        cnt = defaultdict(int)
        
        # BFS/DFS to get all nodes and their distances from c
        def get_distances(u, p, cur_dist, depth_info):
            # cur_dist includes a[u], starts from a[c] when u=c
            # depth_info tracks which subtree of c we're in
            d = cur_dist % k
            cnt[(d, depth_info)] += 1
            for v in adj[u]:
                if v != p and not removed[v]:
                    get_distances(v, u, cur_dist + a[v], depth_info)
        
        # Start from centroid
        # First, count paths where one endpoint is c
        # S(c, v) = dist_c[v], we want dist_c[v] ≡ 0 (mod k)
        
        # Process each subtree separately
        subtree_cnts = []
        
        for v in adj[c]:
            if not removed[v]:
                sub_cnt = defaultdict(int)
                def collect(u, p, cur_dist):
                    d = cur_dist % k
                    sub_cnt[d] += 1
                    for w in adj[u]:
                        if w != p and not removed[w]:
                            collect(w, u, cur_dist + a[w])
                collect(v, c, a[c] + a[v])  # path: c -> v, sum = a[c] + a[v]
                subtree_cnts.append(sub_cnt)
        
        # Also include the centroid itself
        # Paths from c to any node v: sum = dist_c[v]
        # We already handle this by considering c as a special case
        
        # Count pairs (c, v) where dist_c[v] ≡ 0 (mod k)
        # dist_c[c] = a[c], so if a[c] ≡ 0 (mod k), c alone... no wait, we need pairs
        
        # For pair (c, v): S(c, v) = sum from c to v = dist_c[v]
        # dist_c[v] for v in subtree: starts with a[c] + ... 
        # Actually let me redefine: dist_c[u] = sum on path from c to u (both inclusive)
        # So dist_c[c] = a[c]
        
        # For v adjacent to c: dist_c[v] = a[c] + a[v]
        
        # Count (c, v) pairs: need dist_c[v] ≡ 0 (mod k)
        for sub_cnt in subtree_cnts:
            for d, count in sub_cnt.items():
                if d == 0:
                    answer += count
        
        # Count pairs (u, v) where u, v are in different subtrees
        # Need: dist_c[u] + dist_c[v] - a[c] ≡ 0 (mod k)
        # => dist_c[u] + dist_c[v] ≡ a[c] (mod k)
        
        # Aggregate counts
        total_cnt = defaultdict(int)
        for sub_cnt in subtree_cnts:
            for d, count in sub_cnt.items():
                # Find complement
                target = (a[c] - d) % k
                answer += count * total_cnt.get(target, 0)
            
            # Add this subtree to total
            for d, count in sub_cnt.items():
                total_cnt[d] += count
    
    def decompose(u):
        calc_size(u, 0)
        total = sz[u]
        if total == 0:
            return
        c = find_centroid(u, 0, total)
        count_paths_through_centroid(c)
        removed[c] = True
        for v in adj[c]:
            if not removed[v]:
                decompose(v)
    
    decompose(1)
    print(answer)

solve()
