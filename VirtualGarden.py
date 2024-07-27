import random
import datetime

class Plant:
    def __init__(self, name, plant_type, growth_stages, watering_schedule, fertilization_schedule, light_requirement):
        self.name = name
        self.plant_type = plant_type
        self.growth_stages = growth_stages
        self.watering_schedule = watering_schedule
        self.fertilization_schedule = fertilization_schedule
        self.light_requirement = light_requirement
        self.current_stage = 0
        self.water_level = 0
        self.fertilizer_level = 0
        self.health = 100
        self.days_since_last_water = 0
        self.days_since_last_fertilizer = 0
        self.last_checkup = datetime.date.today()
        self.pests = False
        self.disease = False
        self.environment_factors = {"light": "medium", "soil_quality": "normal"}
        self.journal = []

    def water(self):
        """Water the plant."""
        if self.days_since_last_water <= self.watering_schedule:
            self.water_level += 1
            self.health += 5
            self.days_since_last_water = 0
            self.add_to_journal("Watered the plant.")
            print(f"{self.name} watered. Water level: {self.water_level}")
        else:
            print(f"{self.name} is overwatered! Be careful.")
            self.health -= 5

        self.grow()

    def fertilize(self):
        """Fertilize the plant."""
        if self.days_since_last_fertilizer <= self.fertilization_schedule:
            self.fertilizer_level += 1
            self.health += 10
            self.days_since_last_fertilizer = 0
            self.add_to_journal("Fertilized the plant.")
            print(f"{self.name} fertilized. Fertilizer level: {self.fertilizer_level}")
        else:
            print(f"{self.name} has had too much fertilizer. Health may be affected.")
            self.health -= 10

    def grow(self):
        """Grow the plant based on water and health levels."""
        if self.current_stage < len(self.growth_stages) - 1:
            if self.water_level >= self.growth_stages[self.current_stage]["water"] and self.health >= 50:
                self.current_stage += 1
                self.water_level = 0
                self.add_to_journal(f"Plant grew to stage: {self.growth_stages[self.current_stage]['stage']}")
                print(f"{self.name} is now at stage: {self.growth_stages[self.current_stage]['stage']}")
        else:
            print(f"{self.name} is fully grown.")

    def check_environment(self):
        """Check environmental factors and adjust plant health accordingly."""
        # Simulate environmental effects
        if self.environment_factors["light"] != self.light_requirement:
            print(f"{self.name} is not getting the right amount of light.")
            self.health -= 10
        if self.environment_factors["soil_quality"] != "good":
            print(f"{self.name} is in poor soil quality.")
            self.health -= 5

    def check_pests_and_diseases(self):
        """Randomly check for pests and diseases affecting the plant."""
        if random.random() < 0.1:  # 10% chance of pests
            self.pests = True
            print(f"{self.name} has pests! Take action.")
            self.health -= 15
        if random.random() < 0.05:  # 5% chance of disease
            self.disease = True
            print(f"{self.name} has a disease! Treat it immediately.")
            self.health -= 20

    def prune(self):
        """Prune the plant to maintain health."""
        self.health += 10
        self.add_to_journal("Pruned the plant.")
        print(f"{self.name} pruned. Health improved.")

    def add_to_journal(self, entry):
        """Add an entry to the plant's journal."""
        date = datetime.date.today().strftime("%Y-%m-%d")
        self.journal.append(f"{date}: {entry}")

    def display_journal(self):
        """Display the plant's journal."""
        print(f"\nJournal for {self.name}:")
        for entry in self.journal:
            print(entry)

    def pass_day(self):
        """Simulate the passing of a day."""
        self.days_since_last_water += 1
        self.days_since_last_fertilizer += 1
        self.check_environment()
        self.check_pests_and_diseases()
        self.health = max(0, self.health - (1 if self.days_since_last_water > self.watering_schedule else 0))
        self.health = max(0, self.health - (2 if self.days_since_last_fertilizer > self.fertilization_schedule else 0))

        if self.health <= 0:
            print(f"{self.name} has died. Please remove it from the garden.")
        else:
            print(f"{self.name} is at health: {self.health}. Days since last water: {self.days_since_last_water}, fertilizer: {self.days_since_last_fertilizer}")

    def get_status(self):
        return {
            "name": self.name,
            "type": self.plant_type,
            "stage": self.growth_stages[self.current_stage]["stage"],
            "water_level": self.water_level,
            "fertilizer_level": self.fertilizer_level,
            "health": self.health,
            "pests": self.pests,
            "disease": self.disease,
            "environment_factors": self.environment_factors
        }

class VirtualGarden:
    def __init__(self):
        self.plants = []

    def add_plant(self, name, plant_type):
        """Add a new plant to the garden."""
        plant_types = {
            "flower": {
                "growth_stages": [
                    {"stage": "Seed", "water": 1},
                    {"stage": "Sprout", "water": 2},
                    {"stage": "Bud", "water": 3},
                    {"stage": "Bloom", "water": 4}
                ],
                "watering_schedule": 2,
                "fertilization_schedule": 4,
                "light_requirement": "high"
            },
            "tree": {
                "growth_stages": [
                    {"stage": "Seed", "water": 2},
                    {"stage": "Sapling", "water": 4},
                    {"stage": "Young Tree", "water": 6},
                    {"stage": "Mature Tree", "water": 8}
                ],
                "watering_schedule": 5,
                "fertilization_schedule": 10,
                "light_requirement": "medium"
            },
            "vegetable": {
                "growth_stages": [
                    {"stage": "Seed", "water": 1},
                    {"stage": "Sprout", "water": 2},
                    {"stage": "Mature Plant", "water": 3},
                    {"stage": "Harvest", "water": 4}
                ],
                "watering_schedule": 3,
                "fertilization_schedule": 5,
                "light_requirement": "full"
            }
        }
        if plant_type in plant_types:
            plant_info = plant_types[plant_type]
            plant = Plant(name, plant_type, plant_info["growth_stages"], plant_info["watering_schedule"], plant_info["fertilization_schedule"], plant_info["light_requirement"])
            self.plants.append(plant)
            print(f"{name} ({plant_type}) added to the garden.")

    def remove_plant(self, name):
        """Remove a plant from the garden."""
        for plant in self.plants:
            if plant.name == name:
                self.plants.remove(plant)
                print(f"Removed {name} from the garden.")
                return
        print(f"No plant named {name} found in the garden.")

    def water_plant(self, name):
        """Water a specific plant."""
        plant = self.find_plant(name)
        if plant:
            plant.water()

    def fertilize_plant(self, name):
        """Fertilize a specific plant."""
        plant = self.find_plant(name)
        if plant:
            plant.fertilize()

    def prune_plant(self, name):
        """Prune a specific plant."""
        plant = self.find_plant(name)
        if plant:
            plant.prune()

    def find_plant(self, name):
        """Find a plant by name."""
        for plant in self.plants:
            if plant.name == name:
                return plant
        print(f"No plant named {name} found in the garden.")
        return None

    def show_garden(self):
        """Display all plants in the garden."""
        print("\nYour Virtual Garden:")
        for plant in self.plants:
            status = plant.get_status()
            print(f"{status['name']} ({status['type']}) - Stage: {status['stage']}, Health: {status['health']}, Water Level: {status['water_level']}, Fertilizer Level: {status['fertilizer_level']}, Pests: {'Yes' if status['pests'] else 'No'}, Disease: {'Yes' if status['disease'] else 'No'}")

    def pass_day(self):
        """Pass a day in the garden."""
        for plant in self.plants:
            plant.pass_day()

    def journal(self, name):
        """Show the journal of a specific plant."""
        plant = self.find_plant(name)
        if plant:
            plant.display_journal()

def main():
    garden = VirtualGarden()
    while True:
        print("\nVirtual Garden")
        print("1. Add plant")
        print("2. Remove plant")
        print("3. Water plant")
        print("4. Fertilize plant")
        print("5. Prune plant")
        print("6. Show garden")
        print("7. Pass day")
        print("8. View plant journal")
        print("9. Exit")
        choice = input("Choose an option (1-9): ")

        if choice == '1':
            name = input("Enter the name of the plant: ")
            plant_type = input("Enter the type of plant (flower/tree/vegetable): ").lower()
            garden.add_plant(name, plant_type)
        elif choice == '2':
            name = input("Enter the name of the plant to remove: ")
            garden.remove_plant(name)
        elif choice == '3':
            name = input("Enter the name of the plant to water: ")
            garden.water_plant(name)
        elif choice == '4':
            name = input("Enter the name of the plant to fertilize: ")
            garden.fertilize_plant(name)
        elif choice == '5':
            name = input("Enter the name of the plant to prune: ")
            garden.prune_plant(name)
        elif choice == '6':
            garden.show_garden()
        elif choice == '7':
            garden.pass_day()
        elif choice == '8':
            name = input("Enter the name of the plant to view its journal: ")
            garden.journal(name)
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
