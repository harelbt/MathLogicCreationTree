class _node:
    def __init__(self, left, right, key, tag):
        self.left = left
        self.right = right
        self.key = key
        self.tag = tag


class BinaryTree:

    def __init__(self):
        self.root = _node(None, None, "<>", "")
        self._nodes = [""]

    def __check_string_content(self, node_string):
        if type(node_string) is not str:
            return -1
        for i in range(len(node_string)):
            if (node_string[i] != "1") and (node_string[i] != "0"):
                return -1

    def __check_if_node_in_tree(self, node_string):
        if node_string in self._nodes:
            return -1

    def __check_if_tree_has_a_proper_branch(self, node_string):
        longest_branch_length = max(self._nodes, key=len)
        if len(longest_branch_length) + 1 < len(node_string):
            return -1

    def __check_if_empty_string(self, node_string):
        if node_string == "":
            return -1

    def __push_stop_condition(self, node_string, curr_node, tag):
        if len(node_string) == 1:
            if node_string == "1":
                if (curr_node.left is None) or (curr_node.right is not None):
                    return -1
                else:
                    curr_node.right = _node(None, None, node_string, tag)
                    return 0
            if node_string == "0":
                if curr_node.left is not None:
                    return -1
                else:
                    curr_node.left = _node(None, None, node_string, tag)
                    return 0

    def add_node(self, node_string, tag):
        val = self.__check_string_content(node_string)
        if val is not None:
            return val
        val = self.__check_if_node_in_tree(node_string)
        if val is not None:
            return val
        val = self.__check_if_tree_has_a_proper_branch(node_string)
        if val is not None:
            return val
        oper_val = self.__push_node(node_string, self.root, tag)
        if oper_val == 0:
            self._nodes.append(node_string)
            return oper_val

    def __push_node(self, node_string, curr_node, tag):
        val = self.__check_if_empty_string(node_string)
        if val is not None:
            return val
        stop_value = self.__push_stop_condition(node_string, curr_node, tag)
        if stop_value is not None:
            return stop_value
        decision = curr_node.left if node_string[0] == "0" else curr_node.right
        if decision is None:
            return -1
        return self.__push_node(node_string[1:], decision, tag)

    def print_node_list(self):
        print(self._nodes)

    def __str__(self):
        to_print = ""
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            to_print += "\n" + line
        return to_print

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.tag
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.tag
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.tag
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
