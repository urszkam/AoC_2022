class Reader:
    def __init__(self, directory):
        self.directory = directory
        self.data = self.read()
        
        
    def read(self):
        with open(self.directory) as data_input:
            return data_input.readlines()
    

class Directory:
    dir_objs = {}
    current_dir = None
    
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subs = []
        Directory.dir_objs[name] = self
        if Directory.current_dir is not None:
            self.parent = Directory.current_dir
            self.add_to_parent(self)

        
    def add_to_parent(self, directory):
        self.parent.subs.append(directory)
             
             
    @classmethod        
    def add_file(cls, name, size):
        if name not in cls.current_dir.files.keys():
            cls.current_dir.files[name] = int(size)
            
            
    @classmethod
    def change_dir(cls, directory):
        if directory == '..':
            cls.current_dir = cls.current_dir.parent
            print(cls.current_dir.parent.name, cls.current_dir.name)
        else:
            if directory not in cls.dir_objs.keys():
                obj = cls(directory)
            cls.current_dir = cls.dir_objs[directory]
    