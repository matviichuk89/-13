class CHAIR:
    def __init__(self, name, color, price, material):
        self.name = name
        self.color = color
        self.price = price
        self.material = material
    def change_price(self, new_price):
        self.price = new_price
chair1 = CHAIR("Office Chair", "Black", 150, "Leather")
chair2 = CHAIR("Dining Chair", "Brown", 80, "Wood")
chairs = [chair1, chair2]
chair1.change_price(120)
for chair in chairs:
    print(f"Chair Name: {chair.name}, Color: {chair.color}, Price: {chair.price}, Material: {chair.material}")