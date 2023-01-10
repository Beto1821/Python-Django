class Dog:
  
    def __init__(self, name, age , furcolor):
      self.name = name
      self.age = age
      self.furcolor = furcolor


    def bark(self):
      print("Dark!")

mydog = Dog("Fido", 13, "Brown")

print(mydog.age)



mydog.bark()
# mydog.name = "Fido"
# mydog.age = 16
# print(mydog.name)
# print(mydog.age)