from node_search.graph_search import GraphSearch
from node_search.map_data import MapData
from node_search.models import Action


class UniformCostSearch(GraphSearch):
    def _remove_choice(self, frontier):
        shortest = frontier[0]

        for path in frontier:
            if path.cost < shortest.cost:
                shortest = path

        frontier.remove(shortest)

        return shortest

    def _goal_test(self, node, goal):
        return node == goal

    def _get_actions(self, path, frontier):
        node = path.get_last_node()
        actions = []

        for connection in node.connections:
            neighbor = connection.end

            if path.has_node(neighbor):
                continue

            actions.append(Action(neighbor, connection.cost))

        return actions


def run():
    MapData.load_data()

    breath_first_search = UniformCostSearch(MapData.nodes)
    path = breath_first_search.search(MapData.get_node('Arad'), MapData.get_node('Bucharest'))

    print('path: {}'.format(path))


if __name__ == '__main__':
    run()
