class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.current_age = age

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.current_age} days old"

    def get_info(self) -> str:
        return str(self)

    def grow(self, amount: int) -> None:
        self.height += amount

    def age(self, days: int) -> None:
        self.current_age += days


def ft_plant_growth() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    initial_heights = [plant.height for plant in plants]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for day in range(6):
        for plant in plants:
            plant.grow(1)
            plant.age(1)

    print("=== Day 7 ===")
    for i in range(len(plants)):
        print(plants[i].get_info())
        growth = plants[i].height - initial_heights[i]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
