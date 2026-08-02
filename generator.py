#!/usr/bin/env python3
"""
Test case generator for Modular Path Sum problem.
Generates random trees with random values.
"""

import random
import sys

def generate_tree(n):
    """Generate a random tree using Prufer sequence approach."""
    if n == 1:
        return []
    
    # Simple approach: connect each node i (2 to n) to a random node in [1, i-1]
    edges = []
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        edges.append((parent, i))
    
    # Shuffle to make it less structured
    random.shuffle(edges)
    return edges

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generator.py <n> [k] [seed]")
        sys.exit(1)
    
    n = int(sys.argv[1])
    k = int(sys.argv[2]) if len(sys.argv) > 2 else random.randint(1, 10**9)
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else random.randint(0, 10**9)
    
    random.seed(seed)
    
    # Generate vertex values
    a = [random.randint(0, 10**9) for _ in range(n)]
    
    # Generate tree
    edges = generate_tree(n)
    
    # Output
    print(f"{n} {k}")
    print(" ".join(map(str, a)))
    for u, v in edges:
        print(f"{u} {v}")

if __name__ == "__main__":
    main()
