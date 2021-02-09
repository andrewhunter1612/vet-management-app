DROP TABLE IF EXISTS appointments; 
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    archived BOOLEAN
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    address VARCHAR(255) NOT NULL,
    archived BOOLEAN
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL, 
    date_of_birth VARCHAR(255) NOT NULL, 
    animal_type VARCHAR(255) NOT NULL, 
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE appointments(
    id SERIAL PRIMARY KEY, 
    date VARCHAR(255) NOT NULL,
    time VARCHAR(255) NOT NULL,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE,
    additional_notes TEXT
);