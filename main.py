import creation_tree as tree
iff = tree.CreationTree.logic_strings["iff"]
t = tree.CreationTree.gen_tree("((d∧A)" + iff + "A)")
print(t)
s = t.gen_sent()
print(s)