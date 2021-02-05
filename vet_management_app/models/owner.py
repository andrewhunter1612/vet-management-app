class Owner:
    def __init__(self, name, phone_number, address, id=None):
        self.name = name
        self.id = id
        self.phone_number = phone_number
        self.address = address

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def update_address(self, new_address):
        self.address = new_address