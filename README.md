# 🕸️ Graph Theory with Python & NetworkX

A beginner-friendly introduction to graphs in Python using [NetworkX](https://networkx.org/).  
Each script is self-contained, heavily commented, and progressively builds your intuition.

---

## What is a Graph?

A **graph** is a data structure made of two things:

| Concept | Also called | Example |
|---------|-------------|---------|
| **Node** | Vertex | A person, a city, a webpage |
| **Edge** | Link / Connection | A friendship, a road, a hyperlink |

Weights can be attached to both nodes and edges to encode extra meaning (distance, cost, affinity, etc.).

---

## Repository Structure

```
networkx-graphs/
├── 01_basic_graph.py      # Create a graph, add/remove nodes & edges, node weights
├── 02_weighted_edges.py   # Weighted edges + social network ranking scenario
├── 03_plot_a_graph.py     # Visualize graphs with Matplotlib (3 progressive examples)
└── README.md
```

---

## Quick Start

### 1. Install dependencies

```bash
pip install networkx matplotlib
```

### 2. Run the scripts

```bash
python 01_basic_graph.py
python 02_weighted_edges.py
python 03_plot_a_graph.py
```

---

## Core API Cheatsheet

### Creating a graph

```python
import networkx as nx

G = nx.Graph()          # Undirected graph
G = nx.DiGraph()        # Directed graph
```

### Nodes

```python
G.add_node(1)                        # single node
G.add_node(1, weight=5)              # node with attribute
G.add_nodes_from([2, 3, 4])          # multiple nodes
G.remove_node(1)                     # remove one
G.remove_nodes_from([2, 3])          # remove many
```

### Edges

```python
G.add_edge(1, 2)                          # single edge
G.add_edge(1, 2, weight=4.5)             # edge with weight
G.add_edges_from([(1,2), (2,3)])          # multiple edges
G.add_weighted_edges_from([(1,2,4.5)])   # shorthand for weighted bulk add
G.remove_edge(1, 2)
G.remove_edges_from([(1,2), (2,3)])
```

### Inspection

```python
G.number_of_nodes()              # node count
G.number_of_edges()              # edge count
G.nodes(data=True)               # nodes + their attributes
G.edges(data=True)               # edges + their attributes
G.degree(weight='weight')        # weighted degree per node
```

### Visualization

```python
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True)                        # minimal plot
nx.draw(G, with_labels=True,
        node_color="lightblue", node_size=3000,
        font_weight="bold")                          # styled plot

pos = nx.spring_layout(G, seed=42)                  # auto layout (reproducible)
pos = {"A": (0, 1), "B": (1, 1), "C": (0.5, 0)}   # manual layout

nx.draw(G, pos, with_labels=True)                   # draw with custom positions
plt.savefig("graph.png", dpi=150)                   # save to file
plt.show()                                          # display interactively
```

---

## Script Walkthroughs

### `01_basic_graph.py` — Nodes & Node Weights

Builds a 4-node graph and attaches a `weight` attribute to each node.  
**Key takeaway**: any keyword argument in `add_node()` becomes a queryable attribute.

```
Nodes : 4
Edges : 4

  Node 1 → weight = 5
  Node 2 → weight = 3
  Node 3 → weight = 7
  Node 4 → weight = 2
```

---

### `02_weighted_edges.py` — Edge Weights & Social Network

Models a 7-person friend group where edge weights represent affinity (0–10).  
Uses `weighted degree` to rank who is most liked overall.

```
Edges and affinity scores:
  Person 1 ↔ Person 2  →  affinity = 9.0
  ...

Total affinity score per person (weighted degree):
  #1  Person 3  →  score = 18.0
  ...

🏆 Most liked member: Person 3
```

### `03_plot_a_graph.py` — Visualizing Graphs with Matplotlib

Three progressive plots using the same graph, each adding a layer of control:

| Plot | Technique | Key parameter |
|------|-----------|---------------|
| 1 — Basic | Default auto-layout | `nx.draw(G, with_labels=True)` |
| 2 — Styled | Auto-layout + custom size/color | `node_size=3000, node_color="lightblue"` |
| 3 — Positioned | Manual coordinates | `pos = {"Mother": (0.25, 1), ...}` |

**Key takeaway**: the graph data never changes across the three plots — only the visual layout does. Use `spring_layout(seed=42)` for reproducible auto-layouts, and a `pos` dict when you need precise control.

Each plot is also saved as a `.png` file, ready to embed in a README or report.

---

## Concepts Covered

- [x] Undirected graphs
- [x] Node attributes (weights)
- [x] Edge attributes (weights)
- [x] Weighted degree as a centrality proxy
- [ ] Directed graphs *(coming soon)*
- [ ] Shortest path algorithms *(coming soon)*
- [x] Graph visualization with Matplotlib

---

## Resources

- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html)
- [Graph Theory — Wikipedia](https://en.wikipedia.org/wiki/Graph_theory)

---

## License

MIT — free to use, share, and adapt.
