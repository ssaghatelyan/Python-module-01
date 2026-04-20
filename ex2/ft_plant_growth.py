class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def grow(self) -> None:
        self.height += 1.5

    def update_age(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25, 30)
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
