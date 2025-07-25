class DFS:
    def recursive_dfs(self, root):
        """
        Depth-First Search visits every node in a binary tree by going "down" as far as possible before backtracking to visit the nodes on the next path.
        Depth-First Search is typically implemented as a recursive function. It visits new nodes in the tree by making recursive calls. When a recursive call is made, a new call frame is pushed onto the call stack.
        Backtracking occurs whenever a recursive call returns. The call frame is popped off the call stack, and execution returns to the next call frame on the call stack.
        :param root:
        :return:
        """
        if root is None or root.visited:
            return ""
        result = root.value
        for neighor in root.neighbors:
            result = "->".join([result, self.recursive_dfs(neighor)])
        return result

    def recursive_sum_of_nodes(self, root):
        """
        :param root:
        :return: the sum of all nodes in a tree
        """
        if root is None:
            return 0
        total = root.value
        for neighbor in root.neighbors:
            total += self.recursive_sum_of_nodes(neighbor)
        return total

    def recursive_max_node(self, root):
        """
        :param root:
        :return: the maximum value of all nodes in a tree
        """
        if root is None:
            # Remember to return correct type
            return float('-inf')
        max_value = root.value
        for neighbor in root.neighbors:
            max_value = max(max_value, self.recursive_max_node(neighbor))
        return max_value

    def recursive_max_depth_of_tree(self, root):
        """
        :return: max depth of the tree
        """
        if root is None:
            return 0
        depth = 0
        for neighbor in root.neighbors:
            depth = max(depth, 1 + self.recursive_max_depth_of_tree(neighbor))
        return depth

    def recursive_max_depth_path(self, root, current_path=None, max_paths=None, current_depth=0, max_depth=None):
        """
        This function finds the maximum depth path in a tree using recursion.
        :param root:
        :param current_path: List of path values being explored
        :param max_path: List of path values that has the maximum depth found so far
        :param current_depth: Current depth of the path being explored
        :param max_depth: Max depth found so far, stored as a list to allow modification within the recursive calls
        :return: List of all nodes in the maximum depth path
        """
        # Initialize variables if they are None
        if current_path is None:
            current_path = []
        if max_paths is None:
            max_paths = []
        if max_depth is None:
            """
            Why do we use a list for max_depth?
            In recursive functions in Python, integers are immutable. 
            When passed as arguments, any changes made to an integer variable within recursive calls won't affect the original value in the parent calls.
            By using a list (which is mutable), changes to the max_depth value persist across recursive calls. 
            """
            max_depth = [0]

        if root is None:
            return max_paths

        current_path.append(root.value)
        current_depth += 1  # current_depth=1

        if current_depth > max_depth[0]:
            """
            Why do we use an integer for current_depth?
            There's an important distinction between current_depth and max_depth in the recursive function:
            1. current_depth is used to track the depth of the current path being explored. 
               When we pass it to recursive calls, we don't need the modified value to persist back to parent calls. 
               Each recursive call works with its own current_depth value independently.
            2. max_depth needs to be shared and updated across all recursive calls because it represents the maximum depth found so far in the entire tree. 
               Changes to this value need to be visible to all recursive calls.
            """
            max_depth[0] = current_depth
            max_paths.clear()  # clear previous max paths if found deeper path
            max_paths.append(current_path[:])  # Add a copy of current_path to max_paths. We use current_path[:] to create a shallow copy of the list. If we use current_path directly, we would be appending a reference to the same list object, which would change as we backtrack and modify current_path in subsequent recursive calls.
            # max_paths.append vs max_paths.extend - append adds a single element (a list in this case) to max_paths, while extend would add each element of the list as separate elements in max_paths.
        elif current_depth == max_depth[0]:
            max_paths.append(current_path[:])

        for neighbor in root.neighbors:
            # In recursive call, current_depth=1 is passed
            self.recursive_max_depth_path(neighbor, current_path, max_paths, current_depth, max_depth)
            # When recursive call returns, we still want current_depth=1 here
            # We don't need changes from child calls

        current_path.pop()  # Backtrack to explore other paths.
        """
        Why do we use current_path.pop()?
        - When we explore a path down the tree, we add nodes to current_path
        - After exploring all children of a node, we need to remove that node from the path
        - This ensures that when we backtrack to explore other paths, we don't include nodes from previously explored paths
        - By popping the last node, we maintain the correct state of current_path for the next recursive calls
        - This is crucial for correctly tracking the path as we explore different branches of the tree
        - If we didn't pop, current_path would keep growing with nodes from all explored paths, leading to incorrect results
        - This is a form of backtracking, where we remove the last added node to return to the previous state of the path
        This pattern of adding a node before exploring its subtrees and removing it afterward (backtracking) is a common technique in tree traversal algorithms to maintain the correct path state during recursion.
        """
        return max_paths

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

    def recursive_path_sum(self, root, target_sum, current_path=None, target_paths=None):
        """
        This function finds all paths in a binary tree that sum to a given target value.
        :param root: The root node of the tree
        :param target_sum: The target sum to find paths for
        :param current_path: List of path values being explored
        :return: List of all paths that sum to the target value
        """
        if current_path is None:
            current_path = []
        if target_paths is None:
            target_paths = []

        if root is None:
            return target_paths

        current_path.append(root.value)
        if sum(current_path) == target_sum:
            target_paths.append(current_path[:])

        for neighbor in root.neighbors:
            self.recursive_path_sum(neighbor, target_sum, current_path, target_paths)

        current_path.pop()
        return target_paths

    def recursive_binary_search_tree(self, root):
        if root is None:
            return True

        if root.left:
            if root.left.value > root.value or not self.recursive_binary_search_tree(root.left):
                return False

        if root.right:
            if root.right.value < root.value or not self.recursive_binary_search_tree(root.right):
                return False

        return True

    def calculate_tilt(self, root):
        """
        The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. If a node does not have a left child, then the sum of the left subtree is treated as 0. The rule is similar if there the node does not have a right child.
        The tilt of the whole tree is defined as the sum of all nodes' tilt.
        :param root:
        :return:
        """
        total_tilt = [0]

        def _calculate_tilt(node):
            if node is None:
                return 0

            left_sum = _calculate_tilt(node.left)
            right_sum = _calculate_tilt(node.right)

            node_tilt = abs(left_sum - right_sum)
            total_tilt[0] += node_tilt

            return left_sum + right_sum + node.value

        _calculate_tilt(root)
        return total_tilt[0]

    def max_diameter(self, root):
        """
        The diameter of a binary tree is the length of the longest path between any two nodes
        in a tree. This path may or may not pass through the root.
        :param root:
        :return: the number of edges in the longest path
        """
        max_diameter = [0]
        def _max_diameter(node):
            if node is None:
                return 0
            left_depth = _max_diameter(node.left) # left_depth to count the edges from the current node to the deepest leaf in the left subtree
            right_depth = _max_diameter(node.right) # right_depth to count the edges from the current node to the deepest leaf in the right subtree
            max_diameter[0] = max(max_diameter[0], left_depth + right_depth) # left_depth + right_depth to count the edges between left and right subtree across the current node
            return 1 + max(left_depth, right_depth) # +1 to add the edge of the current node to its parent, max(left_depth, right_depth) to propagate the maximum depth of the subtree to its parent
        _max_diameter(root)
        return max_diameter[0]

    def max_unique_value_path(self, root):
        """
        Given a binary tree, find the length of the longest path where each node in the path has a unique value (each node has different value from the other nodes). This path may or may not pass through the root.
        :param root:
        :return: the number of nodes in the longest path
        """
        max_length = [0]
        def _max_unique_value_path(node, current_path):
            if node is None:
                return 0
            if node.value in current_path:
                return 0 # If the value is already in the path, we cannot include this node

            current_path.add(node.value)
            left_length = _max_unique_value_path(node.left, current_path) # left_length to count the edges from the current node to the deepest leaf in the left subtree with unique values, because the edge between current node to its left child is already counted in the left subtree recursive calls with 1+ in the return statement
            right_length = _max_unique_value_path(node.right, current_path) # right_length to count the edges from the current node to the deepest leaf in the right subtree with unique values, because the edge between current node to its right child is already counted in the right subtree recursive calls with 1+ in the return statement
            max_length[0] = max(max_length[0], left_length + right_length)
            current_path.remove(node.value) # Backtrack: remove current node value from the path
            return 1 + max(left_length, right_length) # +1 to count the edge between current node to its parent node, max(left_length, right_length) to propagate the maximum length of the subtree to its parent
        _max_unique_value_path(root, set())
        return max_length[0]

    def max_unique_value_path_another_way(self, root):
        """
        Given a binary tree, find the length of the longest path where each node in the path has a unique value (each node has different value from the other nodes). This path may or may not pass through the root.
        :param root:
        :return: the number of nodes in the longest path
        """
        max_length = [0]
        def _max_unique_value_path(node, current_path):
            if node is None:
                return 0
            if node.value in current_path:
                return 0 # If the value is already in the path, we cannot include this node

            current_path.append(node.value)
            left_length = right_length = 0
            if node.left:
                left_length = 1 + _max_unique_value_path(node.left, current_path)
            if node.right:
                right_length = 1+ _max_unique_value_path(node.right, current_path)
            max_length[0] = max(max_length[0], left_length + right_length)

            print(f"current_path {current_path}")
            print(f"current node {node.value}")
            print(f"left_length + right_length {left_length} + {right_length}")
            print(f"max_length {max_length[0]}")

            current_path.remove(node.value) # Backtrack: remove current node value from the path
            return max(left_length, right_length)
        _max_unique_value_path(root, [])
        return max_length[0]

    def max_universal_value_path(self, root):
        """
        Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
        :param root:
        :return: the number of nodes in the longest path
        """
        max_length = [0]
        def _max_universal_value_path(node):
            if node is None:
                return 0

            # Initialize current paths
            left_depth = right_depth = 0
            # Extend paths if child values match current node value
            if node.left and node.left.value == node.value:
                left_depth = 1 + _max_universal_value_path(node.left) # 1 + to count the edge between current node to its left child
            if node.right and node.right.value == node.value:
                right_depth = 1 +  _max_universal_value_path(node.right) # 1 + to count the edge between current node to its right child
            # Update global max and return current max path
            max_length[0] = max(max_length[0], left_depth + right_depth)
            return max(left_depth, right_depth) # return the max path length extending from the current node to its farthest child with the same value

        _max_universal_value_path(root)
        return max_length[0]

    def valid_tree(self, n, edges):
        """
         given an integer n and a list of undirected edges where each entry in the list is a pair of integers representing an edge between nodes 1 and n. You have to write a function to check whether these edges make up a valid tree.
         A valid tree is a connected graph with no cycles.
         Example1:  n = 4, edges = [[0, 1], [2, 3]]
         Output1: False
         Example2:  n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
         Output2: True
        :param n:
        :param edges:
        :return:
        """
        if n == 0:
            return True

        from collections import defaultdict

        graph = defaultdict(list)
        """
        A defaultdict(list) creates a dictionary that automatically initializes a new empty list [] when accessing a non-existent key, instead of raising a KeyError.
        This is particularly useful for building adjacency lists in graph representations, where each key (node) maps to a list of its neighbors.
        """
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent:
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n



if __name__ == "__main__":
    from Node import Node

    dfs = DFS()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    a.add_neighbor(b)
    a.add_neighbor(c)
    b.add_neighbor(e)
    b.add_neighbor(d)

    # Test the recursive DFS implementation
    result = dfs.recursive_dfs(a)
    assert result == "A->B->E->D->C", f"Expected \"A->B->E->D->C\", but got {result}"

    # Test the recursive sum of nodes implementation
    a.value = 1
    b.value = 2
    c.value = 3
    d.value = 4
    e.value = 5

    total = dfs.recursive_sum_of_nodes(a)
    assert total == 15, f"Expected 15, but got {total}"

    # Test the recursive max node implementation
    max_value = dfs.recursive_max_node(a)
    assert max_value == 5, f"Expected 5, but got {max_value}"

    # Test the recursive max depth of tree implementation
    max_depth = dfs.recursive_max_depth_of_tree(a)
    assert max_depth == 2, f"Expected 2, but got {max_depth}"

    # Test the recursive max depth path implementation
    max_depth_path = dfs.recursive_max_depth_path(a)
    assert max_depth_path == [[1, 2, 5], [1, 2, 4]], f"Expected [1, 2, 5], [1, 2, 4], but got {max_depth_path}"

    # Test the recursive find all paths
    all_paths = dfs.recursive_find_all_paths(a)
    assert all_paths == [[1, 2, 5], [1, 2, 4], [1, 3]], f"Expected [1, 2, 5], [1, 2, 4], [1, 3], but got {all_paths}"

    # Test the recursive path sum
    target_paths = dfs.recursive_path_sum(a, 7)
    assert target_paths == [[1, 2, 4]], f"Expected [1, 2, 4] but got {target_paths}"

    target_paths = dfs.recursive_path_sum(a, 13)
    assert target_paths == [], f"Expected [] but got {target_paths}"

    target_paths = dfs.recursive_path_sum(a, 4)
    assert target_paths == [[1, 3]], f"Expected [1, 3] but got {target_paths}"

    target_paths = dfs.recursive_path_sum(a, 8)
    assert target_paths == [[1, 2, 5]], f"Expected [1, 2, 5] but got {target_paths}"

    # Create a binary search tree for testing
    from BinarySearchTreeNode import BinarySearchTreeNode

    a = BinarySearchTreeNode(4)
    b = BinarySearchTreeNode(2)
    c = BinarySearchTreeNode(6)
    d = BinarySearchTreeNode(1)
    e = BinarySearchTreeNode(3)
    a.left = b
    a.right = c
    b.left = e
    b.right = d

    # Test the recursive binary search tree fasle case
    is_bst = dfs.recursive_binary_search_tree(a)
    assert is_bst == False, f"Expected not a binary search tree but got {is_bst}"

    # Test the recursive binary search tree true case
    b.left = d
    b.right = e
    is_bst = dfs.recursive_binary_search_tree(a)
    assert is_bst == True, f"Expected a binary search tree but got {is_bst}"

    # Test the calculate tile
    """
        4
       /   \
      2     6
     / \
    1   3
    Node 4: |6-6| = 0
    Node 2: |1-3| = 2
    Node 6: |0-0| = 0
    Node 1: |0-0| = 0
    Node 3: |0-0| = 0
    Total tilt = 0 + 2 + 0 + 0 + 0 = 2
    """
    total_tilt = dfs.calculate_tilt(a)
    assert total_tilt == 2, f"Expected 2 but got {total_tilt}"

    # Test the max diameter
    max_diameter = dfs.max_diameter(a)
    assert max_diameter == 3, f"Expected 3, but got {max_diameter}"

    # Test the max unique value path
    """
        4
       /   \
      2     6
     / \     
    1   3     
    The longest path with unique values is 1 -> 2 -> 4 -> 6, which has length 3.
    """
    max_unique_value_path = dfs.max_unique_value_path(a)
    assert max_unique_value_path == 3, f"Expected 3, but got {max_unique_value_path}"

    max_unique_value_path_another_way = dfs.max_unique_value_path_another_way(a)
    assert max_unique_value_path_another_way == 3, f"Expected 3, but got {max_unique_value_path_another_way}"

    # Test the max universal value path
    """
          4
       /     \
      4       4
     / \     / \    
    4   4   4   4           

    The longest path with the same value is 4 -> 4 -> 4 -> 4 , which has length 3.
    """
    a = BinarySearchTreeNode(4)
    b = BinarySearchTreeNode(4)
    c = BinarySearchTreeNode(4)
    d = BinarySearchTreeNode(4)
    e = BinarySearchTreeNode(4)
    f = BinarySearchTreeNode(4)
    g = BinarySearchTreeNode(4)
    a.left = b
    a.right = c
    b.left = e
    b.right = d
    c.left = f
    c.right = g
    max_universal_value_path = dfs.max_universal_value_path(a)
    assert max_universal_value_path == 4, f"Expected 4, but got {max_universal_value_path}"

