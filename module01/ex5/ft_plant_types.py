class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def __str__(self) -> str:
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")
        print()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def __str__(self) -> str:
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self, square_meters: int) -> None:
        print(f"{self.name} provides {square_meters} square meters of shade")
        print()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self) -> str:
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 35, 15, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 800, 3650, 45)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 75, "autumn", "vitamin A")

    print(rose)
    rose.bloom()
    print(tulip)
    tulip.bloom()

    print(oak)
    oak.produce_shade(78)
    print(pine)
    pine.produce_shade(120)

    print(tomato)
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print()
    print(carrot)
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")


if __name__ == "__main__":
    ft_plant_types()
