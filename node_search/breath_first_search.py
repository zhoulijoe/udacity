from node_search.map_data import MapData
from node_search.models import Action
from node_search.tree_search import TreeSearch


class BreathFirstSearch(TreeSearch):
    def _remove_choice(self, frontier):
        shortest = frontier[0]

        for path in frontier:
            if path.cost < shortest.cost:
                shortest = path

        frontier.remove(shortest)

        return shortest

    def _goal_test(self, node, goal):
        return node == goal

    def _get_actions(self, node, frontier):
        actions = []

        for connection in node.connections:
            neighbor = connection.end
            should_add = True

            for frontier_path in frontier:
                if frontier_path.has_node(neighbor):
                    should_add = False
                    break

            if should_add:
                actions.append(Action(neighbor, connection.cost))

        return actions


def run():
    MapData.load_data()

    breath_first_search = BreathFirstSearch(MapData.nodes)
    path = breath_first_search.search(MapData.get_node('Arad'), MapData.get_node('Bucharest'))

    print('path: {}'.format(path))


if __name__ == '__main__':
    run()
