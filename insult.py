class Insult:

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text
    
    def __init__(self, category, text, agreement, origin = None):
        self.category = category
        self.text = text
        self.agreement = agreement
        self.origin = origin
        self.status = False