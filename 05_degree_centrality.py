"""
05_degree_centrality.py
------------------------
Introduction to Degree Centrality — one of the most fundamental metrics
in network analysis.

Degree Centrality measures how connected a node is relative to the rest
of the graph. Formally:

    degree_centrality(v) = degree(v) / (n - 1)

where n is the total number of nodes. The result is a value between 0 and 1:
  - 0 → the node has no connections
  - 1 → the node is connected to every other node in the graph

Real-world uses:
  - Social networks  → identify influencers (many followers/followees)
  - Transport grids  → find critical hubs
  - Collaboration    → spot key researchers or connectors

This script covers two examples:
  1. Uniform centrality  – cycle graph where every node scores equally
  2. Varied centrality   – asymmetric graph + color-coded visualization

Requirements:
  pip install networkx matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 1 — Cycle graph: uniform Degree Centrality
# ───────────────────────────────────────────────────────────────────────────────
# In a directed cycle (1→2→3→4→5→1), every node has exactly one incoming
# and one outgoing edge, so all nodes score the same centrality.
# This is a useful baseline to understand what equal prominence looks like.
# ═══════════════════════════════════════════════════════════════════════════════

G_cycle = nx.DiGraph()
G_cycle.add_nodes_from([1, 2, 3, 4, 5])
G_cycle.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# nx.degree_centrality() returns a dict: {node: centrality_score}
degree_centrality = nx.degree_centrality(G_cycle)

print("Example 1 — Cycle graph (uniform centrality):")
for node, centrality in degree_centrality.items():
    print(f"  Node {node}: {centrality:.2f}")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 2 — Asymmetric graph: varied Degree Centrality + visualization
# ───────────────────────────────────────────────────────────────────────────────
# By changing the edge structure, nodes accumulate different numbers of
# connections, producing a range of centrality scores.
#
# Visualization technique:
#   - color_map maps each node's centrality score to a color
#   - cmap=plt.cm.coolwarm → low centrality = blue, high centrality = red
#   - This makes the most influential nodes immediately visible
# ═══════════════════════════════════════════════════════════════════════════════

G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([
    (1, 2), (1, 3),           # node 1: 2 outgoing
    (2, 3), (2, 4),           # node 2: 1 incoming, 2 outgoing
    (3, 4), (3, 5),           # node 3: 2 incoming, 2 outgoing
    (4, 5),                   # node 4: 2 incoming, 1 outgoing
])

degree_centrality = nx.degree_centrality(G)

print("Example 2 — Asymmetric graph (varied centrality):")
for node, centrality in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True):
    bar = "█" * int(centrality * 20)   # simple ASCII bar for quick comparison
    print(f"  Node {node}: {centrality:.2f}  {bar}")
print()

# Map centrality scores to node colors
color_map = [degree_centrality[node] for node in G.nodes()]

# Compute layout — seed ensures the same arrangement every run
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(7, 5))
plt.title("Degree Centrality — warmer color = more central")

# Draw nodes colored by centrality score
nodes = nx.draw_networkx_nodes(
    G, pos,
    node_color=color_map,
    cmap=plt.cm.coolwarm,   # blue (low) → red (high)
    node_size=800,
)
nx.draw_networkx_labels(G, pos, font_weight="bold")
nx.draw_networkx_edges(G, pos, arrowsize=20, edge_color="gray")

# Add a colorbar so readers can interpret the color scale
plt.colorbar(nodes, label="Degree Centrality")
plt.axis("off")
plt.tight_layout()
plt.savefig("plot_degree_centrality.png", dpi=150)
plt.show()

print("✅ Plot saved as plot_degree_centrality.png")
