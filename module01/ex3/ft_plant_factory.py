class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = [Plant(*data) for data in plant_data]

    print("=== Plant Factory Output ===")

    count = 0
    for plant in plants:
        print(f"Created: {plant}")
        count += 1

    print()
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
