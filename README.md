## Description
his Python program defines a class Neo4jGraph to manage and interact with a Neo4j graph database. It provides methods to:

Connect and disconnect from a Neo4j instance.

Create, read, update, and delete (CRUD) nodes and relationships.

Run Cypher queries programmatically.

Retrieve nodes by label and relationships by type.

This program is useful in any project that needs a graph database interface, like knowledge graphs, social networks, recommendation engines, or semantic search systems. Let me know if you want full documentation or a usage example.

## Requirements

Python 3.x

neo4j Python driver (pip install neo4j)

## Class: Neo4jGraph

Constructor

# Neo4jGraph(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)

Initializes a connection to the Neo4j database using provided credentials.

# Methods

# close()

Closes the active connection to the Neo4j database.

# open()

(Stub) Intended to open a Neo4j connection (method body is placeholder).

# run_query(query, parameters=None)

Executes a Cypher query with optional parameters.

# create_node(label, properties)

Creates a node with the specified label and properties.

# create_relationship(node1, node2, relation, properties=None)

Creates a relationship of the specified type between two nodes.

# update_node(label, node_name, new_properties)

Updates the properties of a node identified by its name and label.

# delete_node(label, node_name)

Deletes a node and its relationships from the graph.

# delete_relationship(node1, node2, relation)

Deletes a specific relationship between two nodes.

# get_nodes(label)

Fetches all nodes with the given label and returns their properties.

# get_relationships(relation)

Fetches all relationships of the specified type and returns connected node names.

## Example Usage
neo = Neo4jGraph("bolt://localhost:7687", "neo4j", "password")

neo.create_node("Person", {"name": "Alice"})
neo.create_node("Person", {"name": "Bob"})
neo.create_relationship("Alice", "Bob", "FRIEND")

relationships = neo.get_relationships("FRIEND")
print(relationships)

neo.close()

## Use Cases

Knowledge graph construction

Social network modeling

Graph-based recommendation systems

Semantic data analysis

## Notes

Ensure your Neo4j server is running and accessible with the correct credentials.

Neo4j Aura or cloud-hosted instances may require using neo4j+s:// or bolt+s:// protocols.

The open() method is defined but not implemented (can be enhanced if needed).

