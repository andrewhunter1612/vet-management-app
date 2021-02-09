from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

vet_1 = Vet("Sarah")
vet_2 = Vet("Dave")
vet_3 = Vet("Steve Smith")
vet_4 = Vet("Luke")
owner_1 = Owner("John", "0123456789", "221B Baker Street")
owner_2 = Owner("Lucy", "0123456789", "221A Baker Street")
owner_3 = Owner("Joe", "0123456789", "1600 Pensylvannia avenue")
owner_4 = Owner("Mike", "0123456789", "Marigold lane")


animal_1 = Animal("My little pony", "23/1/2020", "Horse", owner_1, "A good little horsey", vet_1)
animal_5 = Animal("Jaws", "23/1/2020", "Goldfish", owner_1, "We're gonna need a bigger bowl", vet_1)
animal_2 = Animal("Doggy", "11/1/2020", "Dog", owner_2, "Doesn't like the vet", vet_2)
animal_3 = Animal("Kitty kat", "13/1/2020", "cat", owner_3, "A wee shitebag", vet_3)
animal_4 = Animal("Gerry", "13/2/2020", "Giraffe", owner_4, "Easy to find in a busy shop", vet_4)

vet_repository.save_new_vet(vet_1)
vet_repository.save_new_vet(vet_2)
vet_repository.save_new_vet(vet_3)
vet_repository.save_new_vet(vet_4)

owner_repository.save_new_owner(owner_1)
animal_repository.save_new_animal(animal_1)
owner_repository.save_new_owner(owner_2)
animal_repository.save_new_animal(animal_2)
owner_repository.save_new_owner(owner_3)
animal_repository.save_new_animal(animal_3)
owner_repository.save_new_owner(owner_4)
animal_repository.save_new_animal(animal_4)
animal_repository.save_new_animal(animal_5)

# vet_repository.update_vet(vet_1)
# owner_repository.update_owner(owner_1)
# animal_repository.update_animal(animal_1)

print(animal_repository.select_animal(1))
print(vet_repository.select_vet(1))
print(owner_repository.select_owner(1))

print(animal_repository.select_all_animals())
print(owner_repository.select_all_owners())
print(vet_repository.select_all_vets())

  
