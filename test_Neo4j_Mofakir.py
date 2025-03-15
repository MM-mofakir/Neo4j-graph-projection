from neo4j import GraphDatabase
import pytest
import unittest
# import assertEqual
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Mofakir2')
from lib.Mofakir import   KG_Model
from lib.Neo4j_Mofakir   import Neo4jGraph

class Test_Mofakir(unittest.TestCase): 
  
    def __init__(self, methodName='runTest'):
       super().__init__(methodName)
        # Your initialization code here
       print('initial parameters')
       self.NEO4J_URI='neo4j+s://465ccc57.databases.neo4j.io'
       self.NEO4J_USERNAME='neo4j'
       self.NEO4J_PASSWORD='i_L8bWtvDwJF22938yJ_5wFwbZz7PHmkXYidDbMk1zM'
       self.AURA_INSTANCEID='465ccc57'
       self.AURA_INSTANCENAME='Instance01'

    # def test_run_query(self, query, parameters=None):
    #     """Run a Cypher query in Neo4j."""
    #     Neo4jGraph_1 = Neo4jGraph(self.NEO4J_URI, self.NEO4J_USERNAME, self.NEO4J_PASSWORD)
    #     with Neo4jGraph_1.driver.session() as session:
    #         return session.run(query, parameters or {})

    def test_create_node(self):  #, label, properties
        """Create a node with a given label and properties."""
        print('Create a node with a given label and properties')
        KG_model_1 = KG_Model()
        Neo4jGraph_1 = Neo4jGraph(self.NEO4J_URI, self.NEO4J_USERNAME, self.NEO4J_PASSWORD) 
        
        Neo4jGraph_1.open()
         # """Create a node with a given label and properties."""
        KG_model_1.add_node('1',{'name':'zaki','age':12} )
        Neo4jGraph_1.create_node('persone', {'name':'zaki','age':12} )
          #"""Create a node with a given label and properties."""
        KG_model_1.add_node('2',{'name':'baki','age':32} )
        Neo4jGraph_1.create_node('persone', {'name':'baki','age':32} )
       
        KG_model_1.add_node('3',{'name':'bomarakid','age':22} )
        Neo4jGraph_1.create_node('persone', {'name':'bomarakid','age':22} )
        """Create a edgge with a given  properties."""
        KG_model_1.add_relation('1', '2',None,{'name':'play2','age':12})  
        Neo4jGraph_1.create_relationship( 'zaki', 'baki', 'relation1', {'name':'play2','age':12})
        KG_model_1.add_relation('1', '3',None,{'name':'play3','age':12})  
        Neo4jGraph_1.create_relationship( 'zaki', 'bomarakid', 'relation2', {'name':'play3','age':12})
        
        #add function update mofakir
        Neo4jGraph_1.update_node( 'persone','zaki',{'name':'zaki','age':13} )
        Neo4jGraph_1.delete_relationship(  'zaki', 'bomarakid','relation2' )
        
        Neo4jGraph_1.delete_node( 'persone',{'name':'bomarakid','age':22} )

        Neo4jGraph_1.get_nodes( 'persone')

        Neo4jGraph_1.get_relationships('relation2')
        Neo4jGraph_1.close()

# if __name__ == '__main__':
#   unitest.main()
    


