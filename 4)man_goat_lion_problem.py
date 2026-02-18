from collections import deque
import copy

class BlockWorld:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def get_successors(self, state):
        successors = []

        for i in range(len(state)):
            if len(state[i]) == 0:
                continue

            # Pick top block from stack i
            block = state[i][-1]

            for j in range(len(state)):
                if i != j:
                    new_state = copy.deepcopy(state)

                    # Remove block from stack i
                    new_state[i].pop()

                    # Place block on stack j
                    new_state[j].append(block)

                    successors.append(new_state)

        return successors

    def bfs(self):
        queue = deque([(self.start, [])])
        visited = []

        while queue:
            current, path = queue.popleft()

            if self.goal_test(current):
                return path + [current]

            if current not in visited:
                visited.append(current)

                for successor in self.get_successors(current):
                    queue.append((successor, path + [current]))

        return None


if __name__ == "__main__":
