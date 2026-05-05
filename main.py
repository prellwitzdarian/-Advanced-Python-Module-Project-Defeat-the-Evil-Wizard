import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.is_blocking = False

    def attack(self, opponent):
        damage = random.randint(0, self.attack_power)
        
        if opponent.is_blocking:
            damage = 0
            
        opponent.health = max(opponent.health - damage, 0) 
        
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
        opponent.is_blocking = False  # Reset blocking status after attack
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def special_ability(self, opponent):
        print(f"{self.name} has no special ability.")
    
    def defensive_ability(self):
        print(f"{self.name} has no defensive ability.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        #special abilities
    def special_ability(self, opponent):
        self.power_strike(opponent)
        
    def defensive_ability(self):   
        self.shield_block()
        
    def power_strike(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} uses Power Strike on {opponent.name} for {damage} damage!")
        
    def shield_block(self):
        self.is_blocking = True
        print(f"{self.name} uses Shield Block to reduce incoming damage for the next turn!")
        #healing
    def heal(self):
        amount = self.max_health - self.health
        self.health = self.max_health
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        #special abilities
    def special_ability(self, opponent):
        self.fireball(opponent)
        
    def defensive_ability(self):
        self.magic_shield()
        
    def fireball(self, opponent):
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
    def magic_shield(self):
        self.is_blocking = True
        print(f"{self.name} uses Magic Shield to reduce incoming damage for the next turn!")
        #healing
    def heal(self):
        amount = self.max_health - self.health
        self.health = self.max_health
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__ (self, name):
        super().__init__(name, health=120, attack_power=30)
        #special abilities
    def special_ability(self, opponent):
        self.quick_shot(opponent)
        
    def defensive_ability(self):    
        self.evade()
        
    def quick_shot(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")
    def evade(self):
        self.is_blocking = True
        print(f"{self.name} uses Evade to avoid the next attack!")
        #healing
    def heal(self):
        amount = self.max_health - self.health
        self.health = self.max_health
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")
        
# Create Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        #special abilities
    def special_ability(self, opponent):
        self.holy_strike(opponent)
        
    def defensive_ability(self):    
        self.divine_shield()
        
    def holy_strike(self, opponent):
        damage = self.attack_power + 5
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")
    def divine_shield(self):
        self.is_blocking = True
        print(f"{self.name} uses Divine Shield to reduce incoming damage for the next turn!")
        #healing
    def heal(self):
        amount = self.max_health - self.health
        self.health = self.max_health
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        turn_taken = False
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Special Attack")
        print("3. Defensive Ability")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
            turn_taken = True
        elif choice == '2':
            player.special_ability(wizard)
            turn_taken = True
        elif choice == '3':
            player.defensive_ability()
            turn_taken = True
        elif choice == '4':
            player.heal()
            turn_taken = True
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()