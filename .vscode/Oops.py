class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getDetails(self):
        return self.name + " " + str(self.age)


h = Human("Akash", 21)
t = h.getDetails()
print(t)
