import networkx as nx
import matplotlib.pyplot as plt

new = []
with open('cities.csv') as f:
    lines = f.readline()
    for line in f:
        new.append(line.replace("\n"," ").split(';'))
print(new)


Cities = [['Hadiach', 'Zinkiv', 45],['Zinkiv', 'Hadiach', 45],['Hadiach', 'Lebedyn', 60],
          ['Lebedyn', 'Hadiach', 60],['Hadiach', 'Myrhorod', 61],['Myrhorod', 'Hadiach', 61]]



g = nx.Graph()
for edge in Cities:
    g.add_edge(edge[0], edge[1], weight = edge[2])

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Short way")
plt.show()

def short_way(g, c1, c2, weight=None):
    way = (nx.shortest_path(g, c1, c2, weight))
    lenght = (nx.shortest_path_length(g, c1, c2, weight))
    return way, lenght

print(short_way(g,'Lebedyn','Myrhorod',weight='weight'))


