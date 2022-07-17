import itertools
import matplotlib.pyplot as plt
import community.community_louvain
import networkx

import networkx as nx
import networkx.algorithms.community as nx_algo
from community import community_louvain
from networkx.algorithms.community import greedy_modularity_communities, louvain_partitions, k_clique_communities
from networkx.algorithms.community.centrality import girvan_newman





colors = ['yellow',"orange", "purple" ,'green','blue','red','cyan']

karate = nx.karate_club_graph()
# karate = nx.read_edgelist("soc-karate.txt")
remove_edges = 10
comp = girvan_newman(karate)
count = 1

# visualizing the graph
pos = nx.spring_layout(karate, k=0.1, iterations=30, scale=1.3)
nx.draw_networkx_nodes(karate, pos=pos)
nx.draw_networkx_labels(karate, pos=pos)
nx.draw_networkx_edges(karate, pos=pos, width=2, alpha=1, edge_color='k')
plt.axis("off")
plt.show()

print("**********************************************************************************")
print("Betweenness-based clustering using the Girvan-Newman")

# generating tuples by removing different edges
for communities in itertools.islice(comp, remove_edges):
    print("Edge Removal no. {0}".format(count))
    if count == 3:
        modu = list(sorted(c) for c in communities)
    count = count + 1
    print(tuple(sorted(c) for c in communities))
    print(len(communities))


communities = girvan_newman(karate)
node_groups = []
for com in next(communities):
            node_groups.append(list(com))

# print(node_groups) #test the cluster

color_map = []
for node in karate:
    if node in node_groups[0]:
        color_map.append('blue')
    else:
        color_map.append('green')

pos = nx.spring_layout(karate)
nx.draw_networkx_nodes(karate, pos=pos, node_color=color_map)
nx.draw_networkx_labels(karate, pos=pos)
nx.draw_networkx_edges(karate, pos=pos, width=1, alpha=1, edge_color='k')
plt.axis("off")
plt.show()


print("Modularity score is:{0}".format(nx_algo.modularity(karate, modu)))
print("**********************************************************************************")
print("Modularity Based Clustering")

# implementing modularity bases clustering  maximization

node_groups = []
community = list(greedy_modularity_communities(karate))
count = 0
for comm in community:
    print(sorted(comm))
    node_groups.append(list(comm))

# print(node_groups) #test the cluster

color_map = []
for node in karate:
    for i in range(len(node_groups)):
        if node in node_groups[i]:
            color_map.append(colors[i])

pos = nx.spring_layout(karate)
nx.draw_networkx_nodes(karate, pos=pos, node_color=color_map)
nx.draw_networkx_labels(karate, pos=pos)
nx.draw_networkx_edges(karate, pos=pos, width=1, alpha=1, edge_color='k')
plt.axis("off")
plt.show()



print("Modularity score for mudlarity maximization is:{0}".format( networkx.algorithms.community .modularity(karate, community)))
print("**********************************************************************************")
print("Louvain Modularity Method")

partition = community_louvain.best_partition(karate)

pos = nx.spring_layout(karate)
nx.draw_networkx_nodes(karate, pos, partition.keys(), node_color=list(partition.values()))
nx.draw_networkx_edges(karate, pos, alpha=0.5)
nx.draw_networkx_labels(karate, pos=pos)
plt.axis("off")
plt.show()


print("Modularity score for mudlarity for Louvain Modularity Method  is:{0}".format(community_louvain.modularity(partition, karate)))
print(" ")
print(" ")
print(" ")
print("**********************************************************************************")

print("Clique GuidedCommunity Detection Method")

node_groups = []
community = list(k_clique_communities(karate,k=3))
count = 0
for commn in community:
    print(sorted(commn))
    node_groups.append(list(commn))

# print(node_groups) #test the cluster

color_map = []
for node in karate:
    for i in range(len(node_groups)):
        if node in node_groups[i]:
            color_map.append(colors[i])

pos = nx.spring_layout(karate)
nx.draw_networkx_nodes(karate, pos=pos, node_color=color_map)
nx.draw_networkx_labels(karate, pos=pos)
nx.draw_networkx_edges(karate, pos=pos, width=1, alpha=1, edge_color='k')
plt.axis("off")
plt.show()


print("**********************************************************************************")

