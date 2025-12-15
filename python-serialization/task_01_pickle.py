import pickle

class CustomObject:
    
    def __init__(name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
    
    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            data = pickle.load(f)
        
        return data
