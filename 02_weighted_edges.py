"""
02_weighted_edges.py
--------------------
Demonstrates weighted edges through a social-network scenario.

Scenario
--------
Seven friends want to measure mutual affinity.
  - Each person is a node (1–7).
  - Each edge weight represents affinity on a 0–10 scale
    (10 = very close, 0 = no connection).

Key API used here:
  G.add_weighted_edges_from()  – bulk-add (u, v, weight) tuples
  G.edges(data=True)           – iterate over edges with their attributes
  G.degree(weight='weight')    – weighted degree of each node
"""

import networkx as nx

# ── 1. Build the social graph ─────────────────────────────────────────────────
social_graph = nx.Graph()

social_graph.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

# Each tuple: (person_A, person_B, affinity_score)
social_graph.add_weighted_edges_from([
    (1, 2, 9.0),
    (1, 3, 8.0),
    (1, 4, 3.0),
    (2, 3, 2.0),
    (2, 5, 10.0),
    (3, 6, 7.0),
    (3, 7, 1.0),
    (4, 5, 4.0),
    (4, 6, 5.0),
    (5, 7, 6.0),
    (6, 7, 8.0),
])

# ── 2. Print all edges with their weights ────────────────────────────────────
print("Edges and affinity scores:")
for u, v, attrs in social_graph.edges(data=True):
    print(f"  Person {u} ↔ Person {v}  →  affinity = {attrs['weight']}")

# ── 3. Rank members by total weighted degree ─────────────────────────────────
# Weighted degree = sum of all edge weights connected to a node.
# The person with the highest score is the most "liked" overall.
print("\nTotal affinity score per person (weighted degree):")
ranked = sorted(
    social_graph.degree(weight="weight"),
    key=lambda x: x[1],
    reverse=True,
)
for rank, (person, score) in enumerate(ranked, start=1):
    print(f"  #{rank}  Person {person}  →  score = {score:.1f}")

most_liked = ranked[0][0]
print(f"\n🏆 Most liked member: Person {most_liked}")
