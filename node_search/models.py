class Node:
    def __init__(self, name, connections=None):
        if connections is None:
            connections = []
        self.name = name
        self.connections = connections

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_neighbors(self):
        return [x.end for x in self.connections]


class Connection:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def __repr__(self):
        return '{}'.format(self.end.name)


class Action:
    def __init__(self, node, cost=0):
        self.node = node
        self.cost = cost


class Path:
    def __init__(self, nodes, cost=0):
        self.nodes = nodes
        self.cost = cost

    def get_last_node(self):
        return self.nodes[-1]

    def has_node(self, node):
        return node in self.nodes

    def path_appending(self, node, cost_addition=0):
        new_nodes = list(self.nodes)
        new_nodes.append(node)

        return Path(new_nodes, self.cost + cost_addition)

    def __repr__(self):
        return '{} with cost {}'.format(self.nodes, self.cost)
