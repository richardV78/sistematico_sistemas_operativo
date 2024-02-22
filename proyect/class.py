class Student: 
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major

def _str_ (self):  
    return f"Nombre: {self.name} \n Carrera: {self.major}"  


erving = Student(1, "Erving artola", "ISI")
print(erving)
print(erving.__str__())