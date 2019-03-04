
class People:
    def __init__(self, name, age, height, gender):
        self.Name = name
        self.Age = age
        self.Height = height
        self.Gender = gender


    def IsMale (self):
         if (self.Gender == "male"):
             return True
         else:
             return False

         
        

person1 = People("William", 21, 6, "male")
print(person1.IsMale())

print("This person is", person1.Name, ", he is", person1.Age, "years old, and he is", person1.Height, "feet tall")




class Point:
    def __init__(self, x, y):  
        self.X = x  
        self.Y = y 