class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1.5
    
    def update_age(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25.0, 30)
    plant.show()
    plant_height_before = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.update_age()
        plant.show()

    plant_height_after = plant.height
    growth = plant_height_after - plant_height_before
    print(f"Growth this week: {growth}cm")