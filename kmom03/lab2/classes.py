class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn
    
    @property
    def ssn(self):
        return self.__ssn