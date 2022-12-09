class Reader:
    def __init__(self, directory):
        self.directory = directory
        self.data = []

    def read(self):
        with open(self.directory, "r") as data:
            self.data = data.readlines()


class Stack:
    stack_counter = 0
    stack_dict = {}

    def __init__(self, name):
        self.name = name
        self.crates = ""
        Stack.stack_counter += 1
        Stack.stack_dict[Stack.stack_counter] = self

    def push(self, crates, reversed):
        self.crates += crates[::-1] if reversed else crates

    def pop(self, num):
        pop = self.crates[-num:]
        self.crates = self.crates[:-num]
        return pop

    @classmethod
    def move(cls, stack1, stack2, num, reversed):
        crates = cls.stack_dict[stack1].pop(num)
        cls.stack_dict[stack2].push(crates, reversed)

    @classmethod
    def peek_all(cls):
        tops = ""
        for stack in cls.stack_dict.values():
            tops += stack.crates[-1]
        print(tops)
