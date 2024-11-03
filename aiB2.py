import random

class AI:
    def __init__(self, max_turns):
        """
        Called once before the sim starts. You may use this function
        to initialize any data or data structures you need.
        """
        self.turn = -1
        self.visited_cells = set()  # Tracks cells that have already been visited
        self.current_position = (0, 0)  # Assume starting position as (0, 0)
        self.discovered_goals = set()  # To keep track of discovered goals
        self.discovered_teleports = set()  # To keep track of discovered teleport cells

    def update(self, percepts, msg):
        """
        PERCEPTS:
        Called each turn. Parameter "percepts" is a dictionary containing
        nine entries with the following keys: X, N, NE, E, SE, S, SW, W, NW.
        Each entry's value is a single character giving the contents of the
        map cell in that direction. X gives the contents of the cell the agent
        is in.

        COMMAND:
        This function must return one of the following commands as a string:
        N, E, S, W, U
        """
        self.turn += 1
        print(f"B received the message: {msg}")

        # Update current position in visited cells
        self.visited_cells.add(self.current_position)

        # Check for goals or teleport cells to activate with 'U' and communicate
        cell_content = percepts['X'][0]
        if cell_content in {'0', '1', 'r', 'b', 'o', 'y'}:
            if cell_content.isdigit():
                self.discovered_goals.add(self.current_position)
            elif cell_content in {'o', 'b', 'y', 'p'}:
                self.discovered_teleports.add(self.current_position)
            return 'U', [f"{cell_content} found", self.current_position]  # Activate and share discovery

        # Find unvisited adjacent cells to prioritize
        directions = ['E', 'S', 'W', 'N']  # Prefer different initial directions than aiA
        unvisited_directions = [
            direction for direction in directions
            if (self._next_position(direction) not in self.visited_cells)
        ]

        # Choose an unvisited direction if available, otherwise random move
        if unvisited_directions:
            next_move = random.choice(unvisited_directions)
        else:
            next_move = random.choice(directions)

        # Update current position based on chosen move
        self.current_position = self._next_position(next_move)
        return next_move, "B moving"

    def _next_position(self, direction):
        """Helper function to get the next position based on direction."""
        x, y = self.current_position
        if direction == 'N':
            return (x, y - 1)
        elif direction == 'E':
            return (x + 1, y)
        elif direction == 'S':
            return (x, y + 1)
        elif direction == 'W':
            return (x - 1, y)
