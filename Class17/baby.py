class Adult:
    def __init__(self, name):
        self.name = name
        
    def __add__(self, other):
        print(self.name, "and", other.name, "had a baby!")
        return Adult("Baby")
        
sara = Adult("Sara")
andy = Adult("Andy")

print((andy + sara).name)