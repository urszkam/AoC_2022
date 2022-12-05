class Reader():
    def __init__(self, dir):
        self.dir = dir
        self.data = []
        
    
    def read(self):
        with open(self.dir, 'r') as data:
            self.data = data.readlines()
        
        
    def __iter__(self):
        self.line = 0 
        return self
         
            
    def __next__(self):
        if self.line < len(self.data):
            result = self.data[self.line]
            self.line += 1
            return result
        else:
            raise StopIteration
                

class Stack:
    stack_counter = 0
    stack_dict = {}
    
    
    def __init__(self, name):
        self.name = name
        self.crates = ''
        Stack.stack_counter += 1
        Stack.stack_dict[Stack.stack_counter] = self
        
        
    def push(self, crates, reversed=False):
        self.crates += crates[::-1] if reversed else crates 
      
        
    def pop(self, num):
        pop = self.crates[-num:] 
        self.crates = self.crates[:-num]
        return pop
    
    
    @staticmethod
    def move(cls, stack1, stack2, num, reversed):
        crates = cls.stack_dist[stack1].pop(num)
        cls.stack_dict[stack2].push(crates, reversed)
    
    
    @staticmethod
    def peek_all(cls):
        tops = ''
        for stack in cls.stack_dict.values():
            tops += stack.crates[-1]
        print(tops)
    