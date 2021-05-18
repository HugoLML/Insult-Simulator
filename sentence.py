class Sentence:

    def __str__(self):
        return self.content
    
    def __repr__(self):
        return self.content

    def __init__(self):
        self.insults = []
        self.content = []
        self.text = ''
        self.ListToWrite = []
        self.value = 0