import heapq

class EightPuzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        row, col = divmod(zero_index, 3)

        moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))

        return neighbors

    def manhattan(self, state):
        distance = 0
        for i in range(1, 9):  # skip 0 (blank)
            current_index = state.index(i)
            goal_index = self.goal.index(i)

            current_row, current_col = divmod(current_index, 3)
            goal_row, goal_col = divmod(goal_index, 3)

            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

        return distance

    def a_star(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {}
        g_cost = {self.start: 0}

        while open_list:
            _, current = heapq.heappop(open_list)

            if self.goal_test(current):
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost[current] + 1

                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    came_from[neighbor] = current
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + self.manhattan(neighbor)
                    heapq.heappush(open_list, (f_cost, neighbor))

        return None

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    puzzle = EightPuzzle(start_state, goal_state)
    solution = puzzle.a_star()

    print("Solution Path:")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()

