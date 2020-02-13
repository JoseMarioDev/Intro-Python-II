class Item:
    def __init__(self, description, name):
        self.description = description
        self.name = name

    items = []

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")
