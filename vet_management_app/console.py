from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

vet_1 = Vet("Vetty Voop")
vet_2 = Vet("Davey Dave")
vet_3 = Vet("Stevey Smith")
owner_1 = Owner("Owen Owner", "0123456789", "221B Baker Street")
animal_1 = Animal("Little horsey", "13/1/2020", "Horse", owner_1, "A good little horsey", vet_1)

vet_repository.save_new_vet(vet_1)
vet_repository.save_new_vet(vet_2)
vet_repository.save_new_vet(vet_3)
owner_repository.save_new_owner(owner_1)
animal_repository.save_new_animal(animal_1)

vet_repository.update_vet(vet_1)
owner_repository.update_owner(owner_1)
animal_repository.update_animal(animal_1)

print(animal_repository.select_animal(1))
print(vet_repository.select_vet(1))
print(owner_repository.select_owner(1))

print(animal_repository.select_all_animals())
print(owner_repository.select_all_owners())
print(vet_repository.select_all_vets())

  
