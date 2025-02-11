"""
hej hopp här har vi klasserna Person, Address,Teacher och Student
"""
class Person:
    """
    hej hopp här kör person klassen där vi har namn, ssn och adress(om det har)
    """
    def __init__(self, name, ssn, address=""):
        self.name = name
        self.__ssn = ssn
        self.address = address

    @property
    def ssn(self):
        """
            retunerar ssn
        """
        return self.__ssn

    def set_address(self, address):
        """
            ger en adress
        """
        self.address = address

    def __str__(self):
        if isinstance(self.address, Address):
            return f"Name: {self.name} SSN: {self.ssn} {self.address}"
        return f"Name: {self.name} SSN: {self.ssn}"

class Address:
    """
    hej hopp här kör Address klassen där vi har city, stare och country
    """
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return f"Address: {self.city} {self.state} {self.country}"

class Teacher(Person):
    """
    hej hopp här kör Teacher som har ärvt av klassen person 
    """
    def __init__(self, name, ssn, address=""):
        super().__init__(name, ssn, address)
        self.courses = []

    def add_course(self, course):
        """
            lägger till kurs till lärare
        """
        self.courses.append(course)

    def __str__(self):
        base_str = super().__str__()
        courses_str = ""
        for i, course in enumerate(self.courses):
            if i > 0:
                courses_str += ", "
            courses_str += course

        return f"{base_str} Courses: {courses_str}" if courses_str else base_str

class Student(Person):
    """
    hej hopp här kör Student som har ärvt av klassen person 
    """
    def __init__(self, name, ssn, address=""):
        super().__init__(name, ssn, address)
        self.courses_grades = []

    def add_course_grade(self, course, grade):
        """
            lägger till ett betyg till kurs
        """
        self.courses_grades.append((course, grade))

    def average_grade(self):
        """
            räknar ut och retunerar medelbetyget för kurserna.
        """
        total = 0
        count = 0
        for _, grade in self.courses_grades:
            if grade != "-":
                total += grade
                count += 1
        if count > 0 :
            return total / count
        return 0
