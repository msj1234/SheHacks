class Person():
    def __init__(self, name, age, status, hobby, field):
        self.name = name
        self.age = age
        self.status = status
        self.hobby = hobby
        self.field = field

    def toString(self):
        return self.name + "\nAge: " + self.age + "\nHobbies: " + self.hobby + "\nField of Experience/Interest: " + self.field
