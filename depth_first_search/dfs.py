class DFS:
    def recursive_dfs(self, root):
        """
        Depth-First Search visits every node in a binary tree by going "down" as far as possible before backtracking to visit the nodes on the next path.
        Depth-First Search is typically implemented as a recursive function. It visits new nodes in the tree by making recursive calls. When a recursive call is made, a new call frame is pushed onto the call stack.
        Backtracking occurs whenever a recursive call returns. The call frame is popped off the call stack, and execution returns to the next call frame on the call stack.
        :param root:
        :return:
        """
        if root is None:
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
            max_paths.append(current_path[
                             :])  # Add a copy of current_path to max_paths. We use current_path[:] to create a shallow copy of the list. If we use current_path directly, we would be appending a reference to the same list object, which would change as we backtrack and modify current_path in subsequent recursive calls.
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
            if root.left.value > root.value:
                return False
            if not self.recursive_binary_search_tree(root.left):
                return False

        if root.right:
            if root.right.value < root.value:
                return False
            if not self.recursive_binary_search_tree(root.right):
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
        :return:
        """
        max_diameter = [0]
        def _max_diameter(node):
            if node is None:
                return 0
            left_depth = _max_diameter(node.left)
            right_depth = _max_diameter(node.right)
            max_diameter[0] = max(max_diameter[0], left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        _max_diameter(root)
        return max_diameter[0]

    def max_unique_value_path(self, root):
        """
        Given a binary tree, find the length of the longest path where each node in the path has a unique value (each node has different value from the other nodes). This path may or may not pass through the root.
        :param root:
        :return:
        """
        max_length = [0]
        def _max_unique_value_path(node, current_path):
            if node is None:
                return 0
            if node.value in current_path:
                return 0
            current_path.add(node.value)
            left_length = _max_unique_value_path(node.left, current_path)
            right_length = _max_unique_value_path(node.right, current_path)
            max_length[0] = max(max_length[0], 1 + left_length + right_length)
            """
            In max_unique_value_path (line 240), the 1 + is needed because we're counting paths that go through both subtrees, and the current node acts as a connection point. We count the current node (the 1), the longest path in the left subtree (left_length), and the longest path in the right subtree (right_length).
            In max_diameter (line 220), we don't add 1 because we're counting edges between nodes, not nodes themselves. A path's length in terms of edges is always one less than the number of nodes in that path. For example, a path through 3 nodes has 2 edges.
            """
            current_path.remove(node.value)
            return 1 + max(left_length, right_length)
        _max_unique_value_path(root, set())
        return max_length[0]

    def max_universal_value_path(self, root):
        """
        Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
        :param root:
        :return:
        """
        max_length = [0]
        def _max_universal_value_path(node):
            if node is None:
                return 0
            left_length = _max_universal_value_path(node.left)
            right_length = _max_universal_value_path(node.right)
            left_path = right_path = 0
            if node.left and node.left.value == node.value:
                left_path = left_length + 1
            if node.right and node.right.value == node.value:
                right_path = right_length + 1
            max_length[0] = max(max_length[0], left_path + right_path)
            return max(left_path, right_path)
        _max_universal_value_path(root)
        return max_length[0]



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
     / \     \  
    1   3     2
    The longest path with unique values is 1 -> 2 -> 4 -> 6, which has length 4.
    """
    max_unique_value_path = dfs.max_unique_value_path(a)
    assert max_unique_value_path == 4, f"Expected 4, but got {max_unique_value_path}"
