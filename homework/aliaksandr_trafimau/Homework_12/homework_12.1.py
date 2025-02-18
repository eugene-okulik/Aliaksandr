class Flowers:
    def __init__(self, color, steam_length, price, lifespan):
        self.color = color
        self.steam_length = steam_length
        self.price = price
        self.lifespan = lifespan

    def __repr__(self):
        return (f"Color: {self.color}, Length: {self.steam_length}, "
                f"Price: {self.price}, Lifespan: {self.lifespan}")


class HomeFlowers(Flowers):
    def __init__(self, color, steam_length, price, lifespan, temperature_of_life):
        super().__init__(color, steam_length, price, lifespan)
        self.temperature_of_life = temperature_of_life

    def __repr__(self):
        return (f"Color: {self.color}, Length: {self.steam_length}, "
                f"Price: {self.price}, Lifespan: {self.lifespan}, "
                f"Temperature: {self.temperature_of_life}")


class PoisonedFlowers(Flowers):
    def __init__(self, color, steam_length, price, lifespan, level_of_poison):
        super().__init__(color, steam_length, price, lifespan)
        self.level_of_poison = level_of_poison

    def calculate_fatal_risk(self):
        return self.lifespan * self.level_of_poison

    def describe_risk(self):
        risk_of_death = self.calculate_fatal_risk()
        if risk_of_death < 20:
            return "Not lethal"
        elif 20 <= risk_of_death <= 50:
            return "Dangerous to life"
        else:
            return "Lethal"

    def __repr__(self):
        return (f"Color: {self.color}, Length: {self.steam_length}, "
                f"Price: {self.price}, Lifespan: {self.lifespan}, "
                f"Risk: {self.describe_risk()}")


class WildFlowers(Flowers):
    def __init__(self, color, steam_length, price, lifespan, location):
        super().__init__(color, steam_length, price, lifespan)
        self.location = location

    def __repr__(self):
        return (f"Color: {self.color}, Length: {self.steam_length}, "
                f"Price: {self.price}, Lifespan: {self.lifespan}, "
                f"Location: {self.location}")


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers) if self.flowers else 0

    def sort_flowers(self, attribute):
        valid_attributes = ['color', 'steam_length', 'price', 'lifespan']
        if attribute not in valid_attributes:
            raise ValueError("Attribute not valid")
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def find_flowers(self, min_lifespan=None, max_lifespan=None, color=None):
        results = [flower for flower in self.flowers
                   if (min_lifespan is None or flower.lifespan >= min_lifespan)
                   and   (max_lifespan is None or flower.lifespan <= max_lifespan)
                   and   (color is None or flower.color == color)]
        return results

    def __repr__(self):
        return f"Bouquet with {len(self.flowers)} flowers, total cost: {self.total_cost()}"


home_flower1 = HomeFlowers("Red", 30, 10, 7, "Room Temperature: 20°C")
home_flower2 = HomeFlowers("Yellow", 15, 5, 5, "Room Temperature: 22°C")
home_flower3 = HomeFlowers("Pink", 20, 8, 10, "Room Temperature: 18°C")

poisoned_flower1 = PoisonedFlowers("Black", 50, 25, 10, 8)
poisoned_flower2 = PoisonedFlowers("Dark Red", 45, 20, 8, 5)
poisoned_flower3 = PoisonedFlowers("Purple", 40, 15, 7, 10)

wild_flower1 = WildFlowers("Blue", 25, 3, 20, "Forest")
wild_flower2 = WildFlowers("White", 15, 4, 15, "Countryside Meadow")
wild_flower3 = WildFlowers("Orange", 20, 2, 30, "Mountain Region")


bouquet1 = Bouquet([home_flower1, poisoned_flower2, wild_flower3, wild_flower2, poisoned_flower3])
bouquet2 = Bouquet([poisoned_flower1, wild_flower1, home_flower3])
bouquet3 = Bouquet([home_flower1, poisoned_flower1, home_flower2, wild_flower2])
bouquet4 = Bouquet([poisoned_flower3, wild_flower2, home_flower2])
bouquet5 = Bouquet([wild_flower1, wild_flower3, poisoned_flower2])


print("Bouquet 1:", bouquet1)
print("Bouquet 2:", bouquet2)
print("Bouquet 3:", bouquet3)
print("Bouquet 4:", bouquet4)
print("Bouquet 5:", bouquet5)

print("Average lifespan of Bouquet 1:", bouquet1.average_lifespan())
bouquet1.sort_flowers('color')
print("Bouquet 1 after sorting by color:", bouquet1)
found_flowers = bouquet1.find_flowers(min_lifespan=15)
print("Flowers in Bouquet 1 with lifespan >= 15:", found_flowers)


print(poisoned_flower1)
print(home_flower1)
print(wild_flower3)
