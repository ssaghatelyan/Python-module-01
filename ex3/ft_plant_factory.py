class Plant:
    def __init__(self, name: str, height: float | int, age: int) -> None:
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
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    for plant in plants:
        print("Created:", end=" ")
        plant.show()
