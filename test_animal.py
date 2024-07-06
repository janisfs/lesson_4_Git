class Pet():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        print("Описание:\n"
              f"Имя: {self.name}\n"
              f"Порода: {self.species}\n")



sharik = Pet("Sharik", "Dog")
marsel = Pet("Marsel", "Cat")
axel = Pet("Axel", "Mouse")

sharik.describe()
marsel.describe()
axel.describe()
