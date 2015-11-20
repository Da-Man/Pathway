from nodes_dict import nodes

# Generates all the edges 

# Connect all nodes to their right adjacent node with the jump value of 20
# x axis
#print("X AXIS")
jump_val = 20

for node in nodes:
  for adj_node in nodes:
    node_val = nodes[node][0]
    if (node_val+jump_val, nodes[node][1]) == nodes[adj_node]:
      print 'g.add_edge("'+node+'", "'+adj_node+'", '+str(jump_val)+")"
      #print(node, nodes[node]," connected to ",adj_node, nodes[adj_node])
 
# Connect all nodes to their bottom adjacent node with the jump value of 20
# y axis
#print("Y AXIS")
for node in nodes:
  for adj_node in nodes:
    node_val = nodes[node][1]
    if (nodes[node][0], node_val+jump_val) == nodes[adj_node]:
      print 'g.add_edge("'+node+'", "'+adj_node+'", '+str(jump_val)+")"
      #print(node, nodes[node]," connected to ",adj_node, nodes[adj_node])