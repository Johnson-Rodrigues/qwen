# Solution Explanation: Modular Path Sum

## Problem Analysis

We need to count pairs of vertices (u, v) where the sum of values on the path between them is divisible by k.

A naive O(n²) solution would enumerate all pairs and compute path sums, but this is too slow for n ≤ 2×10⁵.

## Key Insight: Centroid Decomposition

The solution uses **centroid decomposition**, a powerful technique for tree problems involving paths.

### Centroid Properties

A centroid of a tree is a vertex whose removal splits the tree into components, each with at most n/2 vertices. Every tree has at least one centroid.

By recursively decomposing the tree using centroids, we get a decomposition tree of height O(log n).

### Path Classification

Every path in the original tree passes through exactly one "highest" centroid in the decomposition hierarchy. This means:
- We can count each valid path exactly once
- At each centroid c, we only count paths that pass through c

## Algorithm

### Step 1: Find Centroid

For a subtree of size `total`, find a vertex c such that no child subtree has size > total/2.

### Step 2: Count Paths Through Centroid

For centroid c, we count paths (u, v) where:
- u and v are in different subtrees of c (or one equals c)
- The path sum S(u, v) ≡ 0 (mod k)

**Key Formula:**

Let `dist_c[x]` = sum of values on the path from c to x (including both endpoints).

For a path (u, v) passing through c:
```
S(u, v) = dist_c[u] + dist_c[v] - a[c]
```

We want S(u, v) ≡ 0 (mod k), so:
```
dist_c[u] + dist_c[v] ≡ a[c] (mod k)
```

### Step 3: Frequency Map Approach

For each subtree of c:
1. Collect all `dist_c` values modulo k
2. For each value d, find how many nodes have value (a[c] - d) mod k in previously processed subtrees
3. Add to answer
4. Merge current subtree's counts into the total

Also count paths where one endpoint is c itself (when dist_c[v] ≡ 0 mod k).

### Step 4: Recurse

Remove c and recursively process each remaining component.

## Complexity Analysis

- **Time**: O(n log n)
  - Each level of centroid decomposition processes O(n) nodes
  - There are O(log n) levels
  - Within each centroid processing, we use hash maps for O(1) lookups

- **Space**: O(n)
  - Adjacency list: O(n)
  - Recursion stack: O(log n)
  - Frequency maps: O(n) total across all centroids

## Implementation Details

1. **Modulo Handling**: All values are taken modulo k to prevent overflow
2. **Centroid Finding**: Use DFS to compute subtree sizes, then find the centroid
3. **Removed Tracking**: Mark processed centroids to avoid revisiting
4. **Edge Cases**: 
   - k = 1: All pairs are valid (answer = n(n-1)/2)
   - Single node: No pairs exist
   - Large k: Values may be smaller than k, requiring careful modulo arithmetic

## Example Walkthrough

For the first example:
```
4 5
2 3 1 4
Edges: 1-2, 1-3, 2-4
```

Tree structure:
```
    1 (val=2)
   / \
  2   3 (val=1)
  |
  4 (val=4)
(val=3)
```

Centroid decomposition might pick vertex 2 as the first centroid. Processing through centroid 2:
- Subtree containing 1 (and 3): distances from 2 are 5, 6
- Subtree containing 4: distance from 2 is 7
- Check which pairs satisfy the modular condition

Final answer: 2 pairs ((1,2) with sum 5, and (3,4) with sum 10).
