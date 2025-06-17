class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def reset_visited(self):
        self.visited = False

    def __repr__(self):
        return f"Node({self.value})"
