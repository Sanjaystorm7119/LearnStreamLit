import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("User", label="User")
G.add_node("LangChain", label="LangChain\n(LLM App Framework)")
G.add_node("LangGraph", label="LangGraph\n(Graph-based LLM Workflows)")
G.add_node("LangSmith", label="LangSmith\n(Debugging & Observability)")

# Add edges to show relationships
G.add_edge("User", "LangChain", label="builds apps with")
G.add_edge("LangChain", "LangGraph", label="uses for complex workflows")
G.add_edge("LangChain", "LangSmith", label="logs/debugs via")
G.add_edge("LangGraph", "LangSmith", label="debugs via")

# Draw the graph
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=4000, node_color="#D0E1F9", font_size=10, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
plt.title("Relationship Between LangChain, LangGraph, and LangSmith")
plt.axis('off')
plt.show()
