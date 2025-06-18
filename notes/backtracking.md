# When is backtracking used?
## Find all possible solutions
### 1.1 Path finding problems
```python
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
### 1.2 Combination/permutations
```python
def generate_permutations(nums):
    def backtrack(start):
        if start == len(nums):  # Found a complete permutation
            result.append(nums[:])
            return
            
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)  # Recurse
            nums[start], nums[i] = nums[i], nums[start]  # Undo swap
    
    result = []
    backtrack(0)
    return result

def generate_combinations(nums, k):
    def backtrack(start, combo):
        if len(combo) == k:  # Found a valid combination
            result.append(combo[:])
            return
            
        for i in range(start, len(nums)):
            combo.append(nums[i])  # Choose
            backtrack(i + 1, combo)  # Explore
            combo.pop()  # Unchoose
    
    result = []
    backtrack(0, [])
    return result

# Example usage:
nums = [1, 2, 3]
print("Permutations:", generate_permutations(nums))  # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
print("Combinations (k=2):", generate_combinations(nums, 2))  # [[1,2], [1,3], [2,3]]
```
Common applications include:
- Generating all possible arrangements of characters (anagrams)
```python
def find_anagrams(word):
    def backtrack(chars, path):
        if not chars:
            result.append(''.join(path))
            return
        for i in range(len(chars)):
            # Choose
            path.append(chars[i])
            # Explore
            backtrack(chars[:i] + chars[i+1:], path)
            # Unchoose
            path.pop()
            
    result = []
    backtrack(list(word), [])
    return result

# Example: find_anagrams('cat') returns ['cat', 'cta', 'act', 'atc', 'tca', 'tac']
```
- Finding all subsets of elements that sum to a target
```python 
def find_subset_sum(nums, target):
    def backtrack(start, path, curr_sum):
        if curr_sum == target:
            result.append(path[:])
            return
        if curr_sum > target:
            return
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, curr_sum + nums[i])
            path.pop()
            
    result = []
    backtrack(0, [], 0)
    return result

# Example: find_subset_sum([1,2,3,4,5], 7) returns [[2,5], [3,4]]
```
- Solving letter/number puzzles where each letter represents a digit
```python
def find_subset_sum(nums, target):
    def backtrack(start, path, curr_sum):
        if curr_sum == target:
            result.append(path[:])
            return
        if curr_sum > target:
            return
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, curr_sum + nums[i])
            path.pop()
            
    result = []
    backtrack(0, [], 0)
    return result

# Example: find_subset_sum([1,2,3,4,5], 7) returns [[2,5], [3,4]]
```

- Creating game moves like chess positions or Sudoku solutions
```python
def generate_knight_moves(pos, board_size=8):
    def is_valid(x, y):
        return 0 <= x < board_size and 0 <= y < board_size

    def backtrack(x, y, path):
        if len(path) == board_size * board_size:
            result.append(path[:])
            return

        moves = [
            (2,1), (1,2), (-1,2), (-2,1),
            (-2,-1), (-1,-2), (1,-2), (2,-1)
        ]
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in path:
                path.append((new_x, new_y))
                backtrack(new_x, new_y, path)
                path.pop()

    result = []
    backtrack(pos[0], pos[1], [pos])
    return result

# Example: Find knight's tour starting from (0,0)
# Returns list of positions visiting each square exactly once
```

### 1.3 State space exploration
```python
def solve_maze(maze):
    def is_valid(x, y):
        return (0 <= x < len(maze) and 
                0 <= y < len(maze[0]) and 
                maze[x][y] == 0)  # 0 represents open path

    def backtrack(x, y, path):
        if x == len(maze)-1 and y == len(maze[0])-1:  # Found target
            result.append(path[:])
            return
        
        moves = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in path:
                path.append((new_x, new_y))
                backtrack(new_x, new_y, path)
                path.pop()

    result = []
    start = (0, 0)
    backtrack(0, 0, [start])
    return result

# Example usage:
maze = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]  # 0 is path, 1 is wall
paths = solve_maze(maze)  # Returns all possible paths from top-left to bottom-right
```