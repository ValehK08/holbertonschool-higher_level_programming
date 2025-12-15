import pickle

class CustomObject:
    
    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
        except:
            return None
        
        return data
