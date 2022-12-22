from __future__ import annotations


class Node:
    def __init__(self, name, parent_node: Node) -> None:
        self.name = name
        self.parent_node = parent_node
        self.children = {}
        self.files = {}
    
    def add_dir(self, dir: Node) -> None:
        self.children.update({dir.name: dir})
        
    def add_file(self, name: str, size: int) -> None:
        self.files.update({name: size})
    
    def get_size(self):
        size = sum(self.files.values())
        size += sum([x.get_size() for x in self.children.values()])
        return size
    
    def calculate_result(self, res: Result2):
        res.add(self.get_size())
        for x in self.children.values():
            x.calculate_result(res)

class Result:
    def __init__(self) -> None:
        self.result = 0
        self.threshhold = 100000

    def add(self, size):
        if size <= self.threshhold:
            self.result += size
    
    def print_result(self):
        print(f"Result is {self.result}")
        
class Result2:
    def __init__(self, threshhold) -> None:
        self.result = []
        self.threshhold = threshhold
    
    def add(self, size):
        if size >= self.threshhold:
            self.result.append(size)

    def print_result(self):
        print(f"Result2 is {min(self.result)}")

class Tree:
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node

    def get_full_size(self):
        return self.root_node.get_size()
    
    def calculate(self, res : Result):
        self.root_node.calculate_result(res)

class Parser:
    def __init__(self) -> None:
        self.root_node = Node("/", None)

    def parse_input(self, file_name: str) -> Tree:
        current_node : Node = None
        with open(file_name) as f:
            for line in f.readlines():
                line = line.rstrip()
                token = line.split(" ")
                if token[0] == "$":
                    if token[1] == "cd":
                        if token[2] == "..":
                            current_node = current_node.parent_node
                        else:
                            if token[2] == "/":
                                current_node = self.root_node
                            else:
                                current_node = current_node.children[token[2]]
                    if token[1] == "ls":
                        pass
                elif token[0] == "dir":
                    current_node.add_dir(Node(token[1], current_node))
                else:
                    current_node.add_file(token[1], int(token[0]))
        return Tree(self.root_node)
        

tree = Parser().parse_input("input7.txt")

update_size = 30000000
filesystem_size = 70000000
occupied_size = tree.get_full_size()
missing_size = update_size - (filesystem_size - occupied_size)
result1 = Result()
result2 = Result2(missing_size)

tree.calculate(result1)
tree.calculate(result2)

result1.print_result()
result2.print_result()
