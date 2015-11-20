from nodes_dict import nodes

# node generator
for i in nodes:
  # node generator for dijkstra's
  print 'g.add_vertex("'+i+'")'
  # node generator for leaflet.js
  print "var node = L.circle(map.unproject([",nodes[i][0],",",nodes[i][1],"], map.getMaxZoom()), 1, node_path).addTo(map);"