class Owner:
    def __init__(self, name, phone_number, address, id=None, archived=False):
        self.name = name
        self.id = id
        self.phone_number = phone_number
        self.address = address
        self.archived = archived

    def update_archived(self, new_archived):
        self.archived = new_archived
