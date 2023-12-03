class DirNode:
    def __init__(self, label, parent):
        self.label = label
        self.parent = parent
        self.children = dict()
        self.size = 0

    def add_child(self, node):
        self.children[node.label] = node
        node.parent = self


class Tree:
    def __init__(self):
        self.root = DirNode(label="/", parent=None)


with open("input") as data:
    lines = [line.split() for line in data.read().split("\n")]

file_tree = Tree()
current_dirs = [file_tree.root]
small_dirs = {file_tree.root}

for line in lines[1:]:
    # case: dir
    if line[0] == "dir":
        new_dir = DirNode(label=line[1], parent=current_dirs[-1])
        current_dirs[-1].add_child(new_dir)
        small_dirs.add(new_dir)

    # case: file
    elif line[0].isnumeric():
        for dir_node in current_dirs:
            dir_node.size += int(line[0])
            if (dir_node in small_dirs) and dir_node.size > 100000:
                small_dirs.remove(dir_node)

    # case: cd
    elif line[1] == "cd":

        # case: cd ..
        if line[2] == "..":
            current_dirs.pop()

        # case: cd /
        elif line[2] == "/":
            current_dirs = [file_tree.root]

        # case: cd to a child
        else:
            current_dirs.append(current_dirs[-1].children[line[2]])


print(sum(n.size for n in small_dirs))
