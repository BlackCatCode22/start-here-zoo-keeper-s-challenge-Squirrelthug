class Animal:
    # Static class variable to keep track of the number of animals
    numOfAnimals = 0

    def __init__(self, species, name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival):

        self.species = species
        self.name = name
        self.animal_id = animal_id
        self.birth_date = birth_date
        self.color = color
        self.sex = sex
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.date_arrival = date_arrival

        # Increment the static variable when a new object is created
        # this is the only place this field's value should be change
        Animal.numOfAnimals += 1




