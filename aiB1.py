import random

class AI:
    def __init__(self, max_turns):
        """
        Called once before the sim starts. You may use this function
        to initialize any data or data structures you need.
        """
        self.turn = -1

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

        N moves the agent north on the map (i.e. up)
        E moves the agent east
        S moves the agent south
        W moves the agent west
        U uses/activates the contents of the cell if it is usable. For
        example, stairs (o, b, y, p) will not move the agent automatically
        to the corresponding hex. The agent must 'U' the cell once in it
        to be transported.

        The same goes for goal hexes (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
        """

        print(f"B received the message: {msg}")

        self.turn += 1

        # To check if the current cell contains a goal, exit, or teleport
        if percepts['X'][0] in {'0', '1', 'r', 'b'}:
            return 'U', None  # Use or activate the cell
        
        # Complementary random movement strategy for exploration
        preferred_directions = ['E', 'S', 'W', 'N']
        next_move = random.choice(preferred_directions)

        return next_move, "B moving"
