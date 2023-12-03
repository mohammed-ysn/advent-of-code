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
all_dirs = {file_tree.root}

for line in lines[1:]:
    # case: dir
    if line[0] == "dir":
        new_dir = DirNode(label=line[1], parent=current_dirs[-1])
        current_dirs[-1].add_child(new_dir)
        all_dirs.add(new_dir)

    # case: file
    elif line[0].isnumeric():
        for dir_node in current_dirs:
            dir_node.size += int(line[0])

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

unused_space = 70000000 - file_tree.root.size
print(f"Unused space: {unused_space:,}")
extra_space_needed = 30000000 - unused_space
print(f"Space needed: {extra_space_needed:,}")
print(
    min(dir_node.size for dir_node in all_dirs if dir_node.size >= extra_space_needed)
)
