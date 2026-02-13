class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self, amount: int) -> None:
        self.height += amount

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.prize_points}")


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def total_plants(self) -> int:
            return len(self.plants)

        def total_growth(self) -> int:
            return sum(p.height - p.initial_height for p in self.plants)

        def plant_types(self) -> tuple:
            reg = sum(1 for p in self.plants
                      if p.__class__.__name__ == 'Plant')
            flo = sum(1 for p in self.plants
                      if p.__class__.__name__ == 'FloweringPlant')
            pri = sum(1 for p in self.plants
                      if p.__class__.__name__ == 'PrizeFlower')
            return reg, flo, pri

        @staticmethod
        def calculate_score(plants: list) -> int:
            base_score = len(plants) * 10
            height_score = sum(p.height for p in plants)
            prize_score = sum(getattr(p, 'prize_points', 0) for p in plants)
            return base_score + height_score + prize_score

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls) -> tuple:
        alice = cls("Alice")
        bob = cls("Bob")
        bob.add_plant(Plant("Bonsai", 82), silent=True)
        return alice, bob

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    def add_plant(self, plant: Plant, silent: bool = False) -> None:
        if self.validate_height(plant.height):
            self.plants.append(plant)
            if not silent:
                print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self, amount: int) -> None:
        print()
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow(amount)
            print(f"{p.name} grew {amount}cm")

    def get_score(self) -> int:
        return self.GardenStats.calculate_score(self.plants)

    def generate_report(self) -> None:
        print()
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p}")

        stats = self.GardenStats(self.plants)
        print()
        print(f"Plants added: {stats.total_plants()}, "
              f"Total growth: {stats.total_growth()}cm")

        reg, flo, pri = stats.plant_types()
        print(f"Plant types: {reg} regular, {flo} flowering, "
              f"{pri} prize flowers")
        print()


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    print()

    alice, bob = GardenManager.create_garden_network()

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice.help_plants_grow(1)
    alice.generate_report()

    print(f"Height validation test: {GardenManager.validate_height(101)}")
    print(f"Garden scores - Alice: {alice.get_score()}, "
          f"Bob: {bob.get_score()}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    ft_garden_analytics()
