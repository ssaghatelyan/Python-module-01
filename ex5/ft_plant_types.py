class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
            
        if age < 0:
            print(f"{self.name}:  Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = float(age)
            print(f"Age updated: {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

class Flower(Plant):
    def __init__(self, color: str) -> None:
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True