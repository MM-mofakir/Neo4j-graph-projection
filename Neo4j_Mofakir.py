from neo4j import GraphDatabase




class Neo4jGraph:
    def __init__(self,NEO4J_URI,NEO4J_USERNAME,NEO4J_PASSWORD):
        """Initialize the connection to the Neo4j database."""
        print('Initialize the connection to the Neo4j database NEO4J_URI',NEO4J_URI,' NEO4J_USERNAME ',NEO4J_USERNAME,' NEO4J_PASSWORD ',NEO4J_PASSWORD)
        # self.driver = GraphDatabase.driver('neo4j+s://465ccc57.databases.neo4j.io', auth=('neo4j', 'i_L8bWtvDwJF22938yJ_5wFwbZz7PHmkXYidDbMk1zM'))
        NEO4J_URI ='neo4j+ssc://360f7910.databases.neo4j.io'  
        USERNAME ='neo4j'
        PASSWORD ='naXGVP6u45k-3iLuq8PxvZZNX488t5A3TxNJZG7Wb40'
        try:
           self.driver = GraphDatabase.driver(NEO4J_URI, auth=(USERNAME, PASSWORD))
           print('connected================================================')
        except Exception as e: print('======= connection ',e)
        # AUTH = (NEO4J_USERNAME, NEO4J_PASSWORD)
        # with GraphDatabase.driver('neo4j+s://465ccc57.databases.neo4j.io', auth=AUTH) as driver:
        #          driver.verify_connectivity()

    def close(self):
        """Close the Neo4j connection."""
        self.driver.close()
    def open(self):
        """Close the Neo4j connection."""
        self.driver.open()
    def run_query(self, query, parameters=None):
        """Run a Cypher query in Neo4j."""
        # with self.driver.session() as session:
        #     return session.run(query, parameters or {})
        try:
            with self.driver.session(database="neo4j") as session:
                return session.run(query, parameters)
            print('run_query================================================')
        except Exception as e: print('======= run_query ',e)
       
    def create_node(self, label, properties):
        """Create a node with a given label and properties."""
        query = f"CREATE (n:{label} $properties)"
        self.run_query(query, {"properties": properties})


    def create_relationship(self, node1, node2, relation, properties=None):
        """Create a relationship between two nodes."""
        query = f"""
        MATCH (a {{name: $node1}}), (b {{name: $node2}})
        CREATE (a)-[r:{relation} $properties]->(b)
        """
        self.run_query(query, {"node1": node1, "node2": node2, "properties": properties or {}})

    def update_node(self, label, node_name, new_properties):
        """Update properties of a node."""
        query = f"""
        MATCH (n:{label} {{name: $node_name}})
        SET n += $new_properties
        """
        self.run_query(query, {"node_name": node_name, "new_properties": new_properties})

    def delete_node(self, label, node_name):
        """Delete a node and its relationships."""
        query = f"""
        MATCH (n:{label} {{name: $node_name}})
        DETACH DELETE n
        """
        self.run_query(query, {"node_name": node_name})

    def delete_relationship(self, node1, node2, relation):
        """Delete a specific relationship between two nodes."""
        query = f"""
        MATCH (a {{name: $node1}})-[r:{relation}]-(b {{name: $node2}})
        DELETE r
        """
        self.run_query(query, {"node1": node1, "node2": node2})

    def get_nodes(self, label):
        """Retrieve all nodes of a specific label."""
        query = f"MATCH (n:{label}) RETURN n.name, n"
        results = self.run_query(query)
        return [{**record["n"]} for record in results]

    def get_relationships(self, relation):
        """Retrieve all relationships of a specific type."""
        query = f"""
        MATCH (a)-[r:{relation}]-(b)
        RETURN a.name AS node1, type(r) AS relationship, b.name AS node2
        """
        results = self.run_query(query)
        return [{"node1": record["node1"], "relationship": record["relationship"], "node2": record["node2"]} for record in results]

