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

class Teacher(Person):
    def __init__(self, name, ssn, address=""):
        super().__init__(name, ssn, address)
        self.courses = []

    def add_course(self, course):
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
    def __init__(self, name, ssn, address=""):
        super().__init__(name, ssn, address)
        self.courses_grades = []

    def add_course_grade(self, course, grade):
        self.courses_grades.append((course, grade))

    def average_grade(self):
        total = 0
        count = 0
        for course, grade in self.courses_grades:
            if grade != "-":
                total += grade
                count += 1
        if count > 0 :
            return total / count
        return 0
