import uuid

class Entity:
    def __init__(self):
        self.id = self.generate_id()
        self.name = self.id

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def generate_id(self):
        # Generate a unique ID using uuid
        return str(uuid.uuid4())