class CreateCharacter:
    def __init__(self, name, classtype, level):
        self.name = name
        self.classtype = classtype
        self.level = level
    def getname(self):
        return self.name
    def getclass(self):
        return self.classtype
    def getlevel(self):
        return self.level
    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string.")
    def set_class(self, classtype):
        if isinstance(classtype, str):
            self.classtype= classtype
        else:
            raise ValueError("Class must be a string.")
    def set_level(self, level):
        if isinstance(level, int):
            self.level = level
        else:
            raise ValueError("Level must be an integer.")