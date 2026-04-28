class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def inc_grow(self) -> None:
            self._grow_calls += 1

        def inc_age(self) -> None:
            self._age_calls += 1

        def inc_show(self) -> None:
            self._show_calls += 1

        def inc_shade(self):
            self._shade_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self._name}:  Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

        self._stats = self._Stats()

    def grow(self) -> None:
        self._height += 1.5
        self._stats.inc_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.inc_age()

    def show(self) -> None:
        self._stats.inc_show()
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def show_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        self._stats.display()

    def show_shade_stats(self) -> None:
        print("0 shade")

    @staticmethod
    def older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)
        self._shade_count = 0

    def produce_shade(self) -> None:
        self._stats.inc_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def show_shade_stats(self) -> None:
        print(f"{self._stats._shade_calls} shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def display_statics(plant: Plant) -> None:
    plant.show_stats()
    plant.show_shade_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")

    print("\n=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    display_statics(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    display_statics(flower)

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    display_statics(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_statics(tree)

    print("\n=== Seed")
    flower1 = Seed("Sunflower", 80, 45, "yellow")
    flower1.show()
    print("[make sunflower grow, age and bloom]")
    flower1.grow()
    flower1.age()
    flower1.bloom()
    flower1.show()
    display_statics(flower1)

    print("\n=== Anonymous")
    plant = Plant.anonymous()
    plant.show()
    display_statics(plant)
