#!/usr/bin/env python3
"""
Qwen Attempt 3 - Incorrect Frequency Map with Backtracking (INCORRECT)
This attempt tries to use prefix sums with modular arithmetic but incorrectly
manages the frequency map during DFS traversal. It has bugs in counting and
backtracking logic that cause wrong answers.
"""

import sys
from collections import defaultdict

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

    result = 0
    freq = defaultdict(int)
    
    def dfs(node, parent, path_sum):
        nonlocal result
        
        # Calculate current prefix sum mod k
        curr_mod = path_sum % k
        
        # BUG: Wrong counting logic - doesn't properly handle all paths
        result += freq[curr_mod]
        
        # BUG: Missing the case where path from root to current node is valid
        
        # Update frequency map
        freq[curr_mod] += 1
        
        # Process children
        for child in adj[node]:
            if child != parent:
                dfs(child, node, path_sum + a[child])
        
        # BUG: Incorrect backtracking - should decrement but logic is flawed
        freq[curr_mod] -= 1
        # Missing: proper handling of negative counts or removal

    # Start DFS from node 1
    dfs(1, -1, a[1])
    
    print(result)

if __name__ == "__main__":
    solve()
