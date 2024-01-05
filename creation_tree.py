import copy

import bin_tree as tree


class CreationTree (tree.BinaryTree):
    logic_strings = {"iff": "↔", "if_then": "→", "or": "∨", "and": "∧", "not": "¬"}

    def __init__(self):
        super().__init__()

    def _push_node_to(self, node_string, tag):
        if (node_string + "1") in self._nodes:
            return -1
        if (node_string + "0") in self._nodes:
            node_string += "1"
        else:
            node_string += "0"
        return self.add_node(node_string, tag)

    @staticmethod
    def gen_tree(exp_l: str):
        b = {'↔', '→', '∨', '∧'}
        u = {'¬'}
        pa = {'(', ')'}
        l_c = b.union(u).union(pa)
        if len(exp_l) == 0:
            return -1
        if len(exp_l) == 1:
            if exp_l[0] not in l_c:
                t = CreationTree()
                t.root.tag = exp_l
                return t
            else:
                return -1
        elif (exp_l[0] == '(') and (exp_l[-1] == ')'):
            if exp_l[1] == '¬':
                t_ = CreationTree()
                t = CreationTree.gen_tree(exp_l[1:])
                if t == -1:
                    return -1
                t_.root.tag = '¬'
                t_.root.left = t.root
                return t_
            else:
                left_p = 0
                right_p = 0
                bin_index = 0
                for i in range(len(exp_l) - 2):
                    if exp_l[i+1] == '(':
                        left_p += 1
                    if exp_l[i+1] == ')':
                        right_p += 1
                    if left_p == right_p:
                        bin_index = i + 1
                        break
                if exp_l[bin_index + 1] in b:
                    t1 = CreationTree.gen_tree(exp_l[1:bin_index+1])
                    t2 = CreationTree.gen_tree(exp_l[bin_index+2:len(exp_l)-1])
                    if (t1 == -1) or (t2 == -1):
                        return -1
                    t = CreationTree()
                    t.root.tag = exp_l[bin_index + 1]
                    t.root.left = t1.root
                    t.root.right = t2.root
                    return t
                else:
                    return -1
        else:
            return -1

    def gen_sent(self):
        if self.root.left is None:
            return self.root.tag
        if self.root.right is None:
            t = CreationTree()
            t.root = self.root.left
            return '(' + self.root.tag + t.gen_sent() + ')'
        t_l = CreationTree()
        t_l.root = self.root.left
        t_r = CreationTree()
        t_r.root = self.root.right
        return '(' + t_l.gen_sent() + self.root.tag + t_r.gen_sent() + ')'
