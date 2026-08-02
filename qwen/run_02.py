#!/usr/bin/env python3
"""
Qwen Attempt 2 - Root-to-Node Only DFS (INCORRECT)
This attempt only counts paths from root to each node, completely missing
paths between arbitrary pairs of nodes. It will fail on most test cases.
"""

import sys

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

    count = 0
    
    def dfs(node, parent, path_sum):
        nonlocal count
        # Only count paths from root to this node
        if path_sum % k == 0:
            count += 1
            
        for child in adj[node]:
            if child != parent:
                dfs(child, node, path_sum + a[child])

    # Start DFS from root (node 1)
    dfs(1, -1, a[1])
    
    print(count)

if __name__ == "__main__":
    solve()
