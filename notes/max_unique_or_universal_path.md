# Comparison: max_unique_value_path vs max_universal_value_path

## Key Differences

### Problem Definition
- **max_unique_value_path**: Finds longest path where all values must be different from each other
  ```
                 1
               /   \
              2     3
             / \     \
            4   5     2
 
  Longest unique path: 4->2->1->3 (length 4)
   ```

- **max_universal_value_path**: Finds longest path where all values must be the same
```
               5
             /   \
            5     5
           / \     \
          4   5     5
  
  Longest universal path: 5->5->5->5 (length 4)
```

### Implementation Approach

#### max_unique_value_path
```python
def _max_unique_value_path(node, current_path):
    if node.value in current_path:  # Stop if duplicate found
        return 0
    current_path.add(node.value)    # Track history
    left = _max_unique_value_path(node.left, current_path)
    right = _max_unique_value_path(node.right, current_path)
    max_length[0] = max(max_length[0], 1 + left + right)
    current_path.remove(node.value)  # Backtrack
    return 1 + max(left, right)
```

- Uses a set to track path history
- Must backtrack by removing values
- Can use both left and right paths
- Returns nodes in path

#### max_universal_value_path
```python
def _max_universal_value_path(node):
    if node is None:
        return 0
    left = _max_universal_value_path(node.left)
    right = _max_universal_value_path(node.right)
    left_path = right_path = 0
    if node.left and node.left.value == node.value:  # Check matching values
        left_path = left + 1
    if node.right and node.right.value == node.value:
        right_path = right + 1
    max_length[0] = max(max_length[0], left_path + right_path)
    return max(left_path, right_path)
```

- Only needs to check adjacent node values
- No tracking of history needed
- Only extends path for matching values
- Returns length of matching sequence
```