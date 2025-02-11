class Person:
    def __init__(self, name, ssn, address=""):
        self.name = name
        self.__ssn = ssn
        self.address = address
    
    @property
    def ssn(self):
        return self.__ssn
    
    def set_address(self, address):
         self.address = address

    def __str__(self):
            if isinstance(self.address, Address):
                return f"Name: {self.name} SSN: {self.ssn} {self.address}"
            return f"Name: {self.name} SSN: {self.ssn}"

class Address:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
            return f"Address: {self.city} {self.state} {self.country}"