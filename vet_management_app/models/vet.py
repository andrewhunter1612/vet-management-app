class Vet:
    def __init__(self, name, id=None, archived=False):
        self.name = name
        self.id = id
        self.archived = archived

    def update_archived(self, new_archived):
        self.archived = new_archived