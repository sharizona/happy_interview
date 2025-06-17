# When is backtracking used?
## 1. Find all possible solutions
* Path finding problems
* Combination/permutations
* State space exploration
```aiignore
    def recursive_find_all_paths(self, root, current_path=None, paths=None):
        if current_path is None:
            current_path = []
        if paths is None:
            paths = []
        if root is None:
            return paths

        current_path.append(root.value)

        if not root.neighbors:
            paths.append(current_path[:])  # found leaf node, current path complete.

        for neighbor in root.neighbors:
            self.recursive_find_all_paths(neighbor, current_path, paths)

        current_path.pop()
        return paths
```