#Nama	: Agung Sihab Malawi
#Kelas  : R1
#NIM	: 210511047

class Employee:
    def __init__(self, name, age, salary): 
        self.name = name
        self.age = age 
        self.salary = salary
    def get_name(self):
        return self.name
    def get_age(self): 
        return self.age
    def get_salary(self):
        return self.salary 
    def speak(self):
        print(f"{self.name} speaks")

class Manager(Employee):
    def __init__(self, name, age, salary, department): 
        super().__init__(name, age, salary)   
        self.department = department
    def get_department(self): 
        return self.department

class Programmer(Employee):
    def __init__(self, name, age, salary, language): 
        super().__init__(name, age, salary) 
        self.language = language
    def get_language(self): 
        return self.language

# Hierarchical Inheritance
class SeniorProgrammer(Programmer):
    def __init__(self, name, age, salary, language, level): 
        super().__init__(name, age, salary, language) 
        self.level = level
    def get_level(self): 
        return self.level
    def speak(self):
        print(f"{self.name} Berumur {self.age} berpenghasilan {self.salary}/Bulan, karena menguasai bahasa {self.language} level {self.level}.")
        print("="*54)

Pengunjung = SeniorProgrammer("Agung Sihab Malawi", 20,"Rp 1000.000", "Python", 3)
Pengunjung.speak()
