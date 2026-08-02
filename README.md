# Modular Path Sum - Competitive Programming Problem

## Problem Summary

Count pairs of vertices in a tree where the sum of values on the path between them is divisible by k.

## Files Structure

```
/workspace/
├── problem.md           # Full problem statement
├── solution.py          # Optimal O(n log n) solution using centroid decomposition
├── solution_bf.py       # Brute-force O(n²) solution for testing
├── generator.py         # Test case generator
├── idea.md              # Problem development history
├── solution.md          # Solution explanation
├── requirements.json    # Time/memory limits
├── test_cases/          # Test cases (5 cases)
│   ├── 1.in, 1.out
│   ├── ...
│   └── 5.in, 5.out
└── qwen/                # Qwen model attempts (should fail)
    ├── conversations.md
    ├── run_01.py
    ├── run_02.py
    └── run_03.py
```

## Verification

All test cases pass with both optimal and brute-force solutions:
- Test 1: Basic example (answer: 2)
- Test 2: Star graph (answer: 2)  
- Test 3: Edge case with large k (answer: 1)
- Test 4: Line graph (answer: 2)
- Test 5: Balanced tree (answer: 5)

Performance verified up to n = 100,000 within time limits.

## Algorithm

The solution uses **centroid decomposition**:
1. Find centroid of current subtree
2. Count valid paths passing through centroid using frequency maps
3. Recursively process remaining components

Time Complexity: O(n log n)
Space Complexity: O(n)

## Originality

This problem is original and not a rephrasing of existing problems. The combination of:
- Modular arithmetic on path sums
- Centroid decomposition for counting
- The specific formula dist_c[u] + dist_c[v] ≡ a[c] (mod k)

makes this a novel Div1/Div2 difficulty problem.
