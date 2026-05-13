"""
01_basic_graph.py
-----------------
Introduction to graph creation with NetworkX.

A graph is a collection of:
  - Nodes (vertices): the entities in your network
  - Edges (connections): the relationships between entities

Key API used here:
  G.add_node()         – add a single node
  G.add_nodes_from()   – add multiple nodes at once
  G.add_edge()         – add a single edge
  G.add_edges_from()   – add multiple edges at once
  G.nodes(data=True)   – iterate over nodes with their attributes
"""

import networkx as nx

# ── 1. Create an empty undirected graph ──────────────────────────────────────
G = nx.Graph()

# ── 2. Add nodes with a 'weight' attribute ───────────────────────────────────
# Any keyword argument passed to add_node() becomes a node attribute.
G.add_node(1, weight=5)
G.add_node(2, weight=3)
G.add_node(3, weight=7)
G.add_node(4, weight=2)

# ── 3. Add edges between nodes ───────────────────────────────────────────────
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)

# ── 4. Inspect the graph ─────────────────────────────────────────────────────
print(f"Nodes : {G.number_of_nodes()}")
print(f"Edges : {G.number_of_edges()}")
print()

# nodes(data=True) yields (node_id, attribute_dict) tuples
for node, attrs in G.nodes(data=True):
    print(f"  Node {node} → weight = {attrs['weight']}")
