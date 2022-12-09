class Reader:
    def __init__(self, directory):
        self.directory = directory
        self.data = self.read()
        
        
    def read(self):
        with open(self.directory) as data_input:
            return data_input.readlines()
    

class Directory:
    current_dir = None
    
    def __init__(self, name):
        self.parent = Directory.current_dir
        self.name = name
        self.files = {}
        self.subs = []
        if self.parent is not None:
            self.add_to_parent(self)

    def add_to_parent(self, directory):
        self.parent.subs.append(directory)

    @classmethod
    def find_directory(cls, name):
        return f"{cls.current_dir.name}/{name}" if cls.current_dir is not None else name
    @classmethod
    def go_up(cls):
        cls.current_dir = cls.current_dir.parent
            
            
    @classmethod
    def go_down(cls, directory):
            cls.current_dir = directory
    
    
    def count_dir_size(self, total=0):
        if total > 100000: return 0
        elif self.subs:
            for sub in self.subs:
                total += sub.count_dir_size()
            return total
        else:
            return sum(self.files.values())
            
        