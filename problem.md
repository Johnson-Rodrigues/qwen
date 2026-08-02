# Problem: Modular Path Sum

## Problem Statement

You are given a tree with $n$ vertices. Each vertex $i$ has an associated value $a_i$. 

For any two vertices $u$ and $v$, let $\text{path}(u, v)$ denote the unique simple path between them in the tree. Define $S(u, v)$ as the sum of values of all vertices on this path (including both endpoints).

Your task is to count the number of unordered pairs $\{u, v\}$ with $u \neq v$ such that $S(u, v) \equiv 0 \pmod{k}$, where $k$ is a given positive integer.

## Input

The first line contains two integers $n$ and $k$ ($2 \le n \le 2 \cdot 10^5$, $1 \le k \le 10^9$) — the number of vertices and the modulus.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($0 \le a_i \le 10^9$) — the values at each vertex.

Each of the next $n-1$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — an edge of the tree. It is guaranteed that the edges form a tree.

## Output

Output a single integer — the number of unordered pairs $\{u, v\}$ with $u \neq v$ such that the sum of values on the path between $u$ and $v$ is divisible by $k$.

## Examples

### Example 1

**Input:**
```
4 5
2 3 1 4
1 2
1 3
2 4
```

**Output:**
```
2
```

**Explanation:** The tree structure is:
```
    1 (val=2)
   / \
  2   3 (val=1)
  |
  4 (val=4)
(val=3)
```

All paths and their sums:
- (1,2): sum = 2+3 = 5 ≡ 0 (mod 5) ✓
- (1,3): sum = 2+1 = 3 ≡ 3 (mod 5) ✗
- (1,4): sum = 2+3+4 = 9 ≡ 4 (mod 5) ✗
- (2,3): sum = 3+2+1 = 6 ≡ 1 (mod 5) ✗
- (2,4): sum = 3+4 = 7 ≡ 2 (mod 5) ✗
- (3,4): sum = 1+2+3+4 = 10 ≡ 0 (mod 5) ✓

Answer: 2 pairs.

### Example 2

**Input:**
```
3 2
1 1 1
1 2
1 3
```

**Output:**
```
2
```

**Explanation:** The tree is a star with center 1. All paths:
- (1,2): sum = 1+1 = 2 ≡ 0 (mod 2) ✓
- (1,3): sum = 1+1 = 2 ≡ 0 (mod 2) ✓
- (2,3): sum = 1+1+1 = 3 ≡ 1 (mod 2) ✗

Answer: 2 pairs.

### Example 3

**Input:**
```
2 1000000000
0 0
1 2
```

**Output:**
```
1
```

**Explanation:** Only one pair (1,2) with sum = 0+0 = 0, which is divisible by any $k$.

## Constraints

- $2 \le n \le 2 \cdot 10^5$
- $1 \le k \le 10^9$
- $0 \le a_i \le 10^9$
- Time limit: 2 seconds
- Memory limit: 256 MB

## Note

The path between two vertices in a tree is unique. The sum includes the values at both endpoints $u$ and $v$.
