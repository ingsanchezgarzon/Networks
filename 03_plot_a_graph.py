"""
03_plot_a_graph.py
------------------
How to visualize graphs using NetworkX + Matplotlib.

This script walks through three progressively refined plots:
  1. Basic plot              – nx.draw() with default layout
  2. Styled nodes            – custom colors, sizes, and labels
  3. Manual node positioning – full control over where nodes appear

Requirements:
  pip install networkx matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 1 — Basic graph
# ───────────────────────────────────────────────────────────────────────────────
# nx.draw() is the simplest way to render a graph.
# with_labels=True   → show node names
# node_color         → any Matplotlib color string or hex code
# font_weight        → typography weight for labels
# ═══════════════════════════════════════════════════════════════════════════════

G = nx.Graph()

G.add_nodes_from(["A", "B", "C", "D"])
G.add_edges_from([("A", "C"), ("A", "D"), ("B", "C"), ("B", "D")])

plt.figure(figsize=(5, 4))
plt.title("Plot 1 — Basic graph")
nx.draw(G, with_labels=True, node_color="lightblue", font_weight="bold")
plt.tight_layout()
plt.savefig("plot1_basic.png", dpi=150)
plt.show()


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 2 — Styled nodes (size + color + meaningful labels)
# ───────────────────────────────────────────────────────────────────────────────
# spring_layout() automatically computes a visually balanced node arrangement.
# node_size          → area of each node circle (default is 300)
# ═══════════════════════════════════════════════════════════════════════════════

G2 = nx.Graph()

G2.add_nodes_from(["Mother", "Father", "Son", "Daughter"])
G2.add_edges_from([
    ("Mother", "Son"),
    ("Mother", "Daughter"),
    ("Father", "Son"),
    ("Father", "Daughter"),
])

pos_auto = nx.spring_layout(G2, seed=42)   # seed → reproducible layout

plt.figure(figsize=(6, 5))
plt.title("Plot 2 — Styled nodes")
nx.draw(
    G2, pos_auto,
    with_labels=True,
    node_color="lightblue",
    node_size=3000,
    font_weight="bold",
)
plt.tight_layout()
plt.savefig("plot2_styled.png", dpi=150)
plt.show()


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 3 — Manual node positioning
# ───────────────────────────────────────────────────────────────────────────────
# Pass a dict of {node: (x, y)} to the `pos` parameter to place nodes exactly
# where you want them.  Coordinates are in data space (any scale works).
#
# Here:  parents  → top row  (y = 1)
#        children → bottom row (y = 0)
# ═══════════════════════════════════════════════════════════════════════════════

pos_manual = {
    "Mother":   (0.25, 1),
    "Father":   (0.75, 1),
    "Son":      (0.25, 0),
    "Daughter": (0.75, 0),
}

plt.figure(figsize=(6, 5))
plt.title("Plot 3 — Manual positioning")
nx.draw(
    G2, pos_manual,
    with_labels=True,
    node_color="lightblue",
    node_size=3000,
    font_weight="bold",
)
plt.tight_layout()
plt.savefig("plot3_manual_positions.png", dpi=150)
plt.show()

print("✅ All three plots saved as PNG files.")
