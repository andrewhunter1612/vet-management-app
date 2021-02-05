DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    address VARCHAR(255) NOT NULL
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL, 
    date_of_birth VARCHAR(255) NOT NULL, 
    animal_type VARCHAR(255) NOT NULL, 
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    treatment_notes TEXT
);

