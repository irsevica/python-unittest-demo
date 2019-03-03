import os

class Phonebook:
    def __init__(self, cachedir):
        self.entries = {}
        self.filename = "phonebook.txt"
        self.file_cache = open(os.path.join(str(cachedir), self.filename), "w")
        
    def add(self, name, number):
        self.entries[name] = number
        
    def lookup(self, name):
        return self.entries[name]
    
    def is_consistent(self):
        if len(self.get_numbers()) != len(set(self.get_numbers())):
            return False
        
        return True
    
    def get_names(self):
        return list(self.entries.keys())
        
    def get_numbers(self):
        return list(self.entries.values())
    
    def clear(self):
        self.entries = {}
        self.file_cache.close()
        os.remove(self.filename)