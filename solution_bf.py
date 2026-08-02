#!/usr/bin/env python3
"""
Brute-force solution for Modular Path Sum problem.
O(n^2) complexity - used for testing correctness.
"""

import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input_data[idx])
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Compute path sum between any two nodes using BFS/DFS
    def get_path_sum(start, end):
        # BFS to find path and compute sum
        from collections import deque
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
        
        # Reconstruct path and compute sum
        path_sum = 0
        cur = end
        while cur != start:
            path_sum += a[cur]
            cur = parent[cur]
        path_sum += a[start]
        return path_sum
    
    answer = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            s = get_path_sum(u, v)
            if s % k == 0:
                answer += 1
    
    print(answer)

solve()
