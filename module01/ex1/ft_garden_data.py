class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(plant1)
    print(plant2)
    print(plant3)


if __name__ == "__main__":
    ft_garden_data()
