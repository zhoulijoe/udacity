from node_search.models import Path


class GraphSearch:
    def __init__(self, data):
        self.data = data

    def _remove_choice(self, frontier):
        return frontier.pop()

    def _goal_test(self, node, goal):
        return False

    def _get_actions(self, path, frontier):
        return []

    def _take_action(self, path, action):
        return path.path_appending(action.node, action.cost)

    def search(self, start, goal):
        initial_path = Path([start])
        frontier = [initial_path]

        while frontier:
            print('frontier: {}'.format(frontier))

            path = self._remove_choice(frontier)
            node = path.get_last_node()

            if self._goal_test(node, goal):
                return path

            for action in self._get_actions(path, frontier):
                frontier.append(self._take_action(path, action))

        return None
