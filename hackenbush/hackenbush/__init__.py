import networkx as nx

def remove_disconnected(graph, root):
    comp = nx.connected.node_connected_component(graph, root)
    g = graph.copy()
    g.remove_nodes_from([n for n in graph if n not in comp])
    return g

class Game:
    def __init__(self, root_key, root_x, root_y):
        self.graph = nx.MultiGraph()
        self.root_key = root_key
        self.add_node(root_key, root_x, root_y)
    
    def add_node(self, key, x, y):
        self.graph.add_node(key, x=x, y=y)
        
    def add_edge(self, start, end, team):
        self.graph.add_edge(start, end, team=team)
    
    def cut(self, start, end, edge_idx, team):
        assert self.graph[start][end][edge_idx].get('team') == team
        g = self.graph.copy()
        g.remove_edge(start, end, edge_idx)
        self.graph = remove_disconnected(g, self.root_key)

    def serialize(self):
        nodes = list(self.graph._node.items())
        
        edges = []
        for start, rest in self.graph._adj.items():
            for end, rest in rest.items():
                if start > end:
                    continue
                for edge_idx, attrs in rest.items():
                    item = {'start': start,
                            'end': end,
                            'edge_idx': edge_idx}
                    item.update(attrs)
                    edges.append(item)
        
        return {'nodes': nodes, 'edges': edges}