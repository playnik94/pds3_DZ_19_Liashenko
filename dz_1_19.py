import networkx as nx
import matplotlib.pyplot as plt

with open('cities.csv') as f:
    lines = f.readlines()
    for line in lines:
        print(str(line).replace("\n", " ").split(";"))


Cities = [['Hadiach', 'Zinkiv', 45],['Zinkiv', 'Hadiach', 45],['Hadiach', 'Lebedyn', 60],
          ['Lebedyn', 'Hadiach', 60],['Hadiach', 'Myrhorod', 61],['Myrhorod', 'Hadiach', 61]]


g = nx.Graph()
for edge in Cities:
    g.add_edge(edge[0], edge[1], weight = edge[2])

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Random Graph Generation Example")
plt.show()

print(nx.shortest_path(g, 'Hadiach', 'Myrhorod', weight='weight'))
print(nx.shortest_path_length(g, 'Hadiach', 'Myrhorod', weight='weight'))
nx.draw_networkx(g)