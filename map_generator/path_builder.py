from nodes_dict import nodes

# The following list was generated through Dijkstra's algorithm
shortest_path = ['c1', 'c38', 'c75',
'c112', 'c148', 'c184', 'c220', 'c225', 'c230', 'c264', 'c298', 'c332',
'c366', 'c400', 'c434', 'c467', 'c500', 'c533', 'c566', 'c599', 'c632',
'c665', 'c666', 'c667', 'c668', 'c669', 'c702', 'c734', 'c766', 'c798',
'c830', 'c862', 'c894', 'c926', 'c958', 'c990', 'c1022', 'c1056',
'c1090', 'c1124', 'c1158', 'c1159', 'c1160', 'c1161', 'c1162', 'c1163',
'c1164', 'c1165', 'c1166', 'c1167', 'c1184', 'c1201', 'c1202', 'c1203',
'c1238', 'c1273', 'c1308', 'c1309', 'c1344', 'c1345', 'c1380', 'c1381',
'c1382', 'c1383', 'c1384', 'c1385', 'c1386', 'c1387', 'c1422', 'c1423',
'c1424', 'c1425', 'c1426', 'c1427', 'c1428', 'c1429', 'c1464', 'c1499',
'c1500']

# Generate the shortest path for leaflet.js
for node in shortest_path:
  print "map.unproject([",nodes[node][0],", ",nodes[node][1],"], map.getMaxZoom()),"