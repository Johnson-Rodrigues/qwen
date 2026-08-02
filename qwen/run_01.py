#!/usr/bin/env python3
"""
Qwen Attempt 1 - Naive O(n^2) solution that will TLE on large inputs.
This is an intentional failing attempt.
"""

import sys
from collections import deque

sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    def get_path_sum(start, end):
        visited = [False] * (n + 1)
        parent = [0] * (n + 1)
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            if u == end:
                break
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        
        path_sum = 0
        cur = end
        while cur != start:
            path_sum += a[cur]
            cur = parent[cur]
        path_sum += a[start]
        return path_sum
    
    ans = 0
    # O(n^2) - will timeout on large inputs
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            s = get_path_sum(u, v)
            if s % k == 0:
                ans += 1
    
    print(ans)

solve()
