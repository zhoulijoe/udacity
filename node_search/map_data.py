from node_search.models import Node, Connection
from node_search.sample_data import MAP_DATA


class MapData:
    nodes = []

    @classmethod
    def load_data(cls):
        for (node_name, node_data) in MAP_DATA.items():
            cls.nodes.append(Node(node_name))

        for node in cls.nodes:
            paths = MAP_DATA[node.name]['paths']
            for (end_name, path_data) in paths.items():
                end_node = cls.get_node(end_name)

                connection = Connection(node, end_node, path_data['distance'])
                node.add_connection(connection)

    @classmethod
    def get_node(cls, name):
        try:
            index = cls.nodes.index(Node(name))

            return cls.nodes[index]
        except ValueError:
            return None
