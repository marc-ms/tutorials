# OOP
'''
string = 'hello'
print(string.upper()) ## .upper() es un METODO. lo identifiacamos por el punto y los parentesis. Este metodo actua sobre el objeto string

 Los metodos dependen del tipo de clase de cada objeto. upper no funcionaria con un int pq int no tiene esos atributos'''


'''
class Dog:

    def __init__(self, name, age): # permite instanciar el objeto justo al crearlo. CREO ENTENDER: self tambien nos permite usar parametros entre metodos, es decir, parametros definidos en un metodo y usarlos en otro
        self.name = name # hemos creado un atributo de la clase dog que llamamos name
        self.age = age # creamos el atributo age
        

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog('Tim', 34) # asignamos l variable d a una instancia de la clase Dog. Instanciar. Creamos una nueva instancia de la clase DOG. d PASA A SER UN OBJETO DE TIPO Dog.
d.set_age(23)
print(d.get_name(), d.get_age())

'''

'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # ojo lista

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student('Sara', 19, 95)
s2 = Student('Marc', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2) # creamos la variable course de nuestra clase Course para usarla con dos estudiantes de Ciencias
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.add_student(s3))
print(course.get_average_grade()) 

'''

######### INHERETANCE (HERENCIA) . idea: tenemos dos clases muy parecidas


# NOS DAMOS CUENTA DE QUE LAS OTRAS CLASES SON PARECIDAS Y CREAMOS ESTA PARA MEJORAR EL CODIGO. esta clase contendra la funcionalidad basica de las otras dos clases y en las otras solo tendremos los metodos y atributos que seran distintos para estas clases especificas
# general class
'''
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet): # añadiendo la clase Pet esta inhereting (heredando) la 'upper level class', es decir, la clase superior
    #def __init__(self, name, age):
    #    self.name = name
    #    self.age = age

    def __init__(self, name, age, color): # ahora lo ponemos pq queremos añadir un atributo a la clase, pero va a ser un init distinto de lo habitual ya que en realidad lo hereda de Pet
        super().__init__(name, age) # super viene de Superclass y esto tenemso que usarlo ya que Cat hereda las propiedades name,age de Pet. Ademas, no necesitamso self
        self.color = color
    
    def speak(self):
        print('meow')
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# la otra clase parecida
class Dog(Pet):
   # def __init__(self, name, age):
    #    self.name = name
    #    self.age = age
    
    def speak(self):
        print('bark') # la unica diferencia es este print POR LO TANTO LO QUE PODEMOS HACER ES MANTENER LAS PARTES QUE DIFIEREN Y QUITAR LA OTRA CREANDO UNA CLASE MAS GENERAL

p = Pet('tim', 30)
p.show()
c = Cat('bill', 40, 'blue')
c.show() # no existe este metodo en la clase cat pero lo hereda de la clase Pet

'''


######## Class Attributes atributos que hacen referencia a las clase no a los objetos de la clase


# lo bueno de usar estos atributos por clase en lugar de una variable globbal fuera de la clase es que son exportables es decir las podemos usar entre scripts
'''
class Person():
    number_of_people = 0 # ESTE es el atributo concreto de la clase

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1 # tenemos qu eponer la clase y el atributo 


p1 = Person('tim')
p2 = Person('jim')

'''

######## Class Methods estos metodos no actuan en nombre de una instancia, sera llamdo por la propia clase, es decir, ACTUAN SOBRE LA PROPIA CLASE, no tienen acceso sobre ninguna instancia y por eso no usamos self pq no hay objeto solo actua en la clase
'''
class Person():
    number_of_people = 0 # ESTE es el atributo concreto de la clase

    def __init__(self, name):
        self.name = name
        Person.add_person()


    @classmethod # usamos un DECORATOR para denotar que este metodo es un metodo de la clase
    def number_of_people_(cls): # metodo de la clase
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('tim')
p2 = Person('jim')
print(Person.number_of_people_())

'''


######## Static Methods


class Math:

    @staticmethod
    def add5(x): # es una funcion que va a actuar solo dentro de esta clase
        return x + 5

print(Math.add5(5))
