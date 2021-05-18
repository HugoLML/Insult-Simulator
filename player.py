class Player:

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __init__(self, name, description, weakness, image):
        
        self.name = name
        self.description = description
        self.weakness = weakness
        self.image = image
        self.status = False