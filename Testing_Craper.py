# from santok_cognitive.graph import GraphStore, GraphNode, RelationType

# # Create graph
# graph = GraphStore()

# # Add nodes
# graph.add_node(GraphNode(1, "dog", node_type="entity"))
# graph.add_node(GraphNode(2, "animal", node_type="concept"))
# graph.add_node(GraphNode(3, "cat", node_type="entity"))

# # Add relationships
# graph.add_edge(1, 2, RelationType.IS_A)  # dog IS_A animal
# graph.add_edge(3, 2, RelationType.IS_A)  # cat IS_A animal

# # Find path
# path = graph.find_path(1, 3)
# print(graph.get_stats())

# # Add nodes
# graph.add_node(GraphNode(1, "Cricket", node_type="entity"))
# graph.add_node(GraphNode(2, "Sport", node_type="concept"))
# graph.add_node(GraphNode(3, "Tennis", node_type="entity"))

# # Add relationships
# graph.add_edge(1, 2, RelationType.IS_A)  # dog IS_A animal
# graph.add_edge(3, 2, RelationType.IS_A)  # cat IS_A animal

# # Find path
# path = graph.find_path(1, 3)
# print(graph.get_stats())



from santok_cognitive.graph import GraphStore, GraphNode, RelationType

graph = GraphStore()

# First domain
graph.add_node(GraphNode("uid_dog", "dog", node_type="entity"))
graph.add_node(GraphNode("uid_animal", "animal", node_type="concept"))
graph.add_node(GraphNode("uid_cat", "cat", node_type="entity"))

graph.add_edge("uid_dog", "uid_animal", RelationType.IS_A)
graph.add_edge("uid_cat", "uid_animal", RelationType.IS_A)

print(graph.get_stats())

# Second domain (different UIDs)
graph.add_node(GraphNode("uid_cricket", "cricket", node_type="entity"))
graph.add_node(GraphNode("uid_sport", "sport", node_type="concept"))
graph.add_node(GraphNode("uid_tennis", "tennis", node_type="entity"))

graph.add_edge("uid_cricket", "uid_sport", RelationType.IS_A)
graph.add_edge("uid_tennis", "uid_sport", RelationType.IS_A)

print(graph.get_stats())
