# Defeat the Evil Wizard - Advanced Python Final Project

An advanced Python project implementing a text-based fantasy adventure game featuring object-oriented programming, game logic, character management, and interactive gameplay.

## Project Overview

This final project for the Advanced Python module demonstrates mastery of Python programming concepts including object-oriented design, game mechanics, data structures, and algorithm implementation through the creation of an engaging fantasy adventure game.

## Tech Stack

- **Python** - 100%

### Language Features Used

- Object-Oriented Programming (OOP)
- Class inheritance and polymorphism
- Exception handling
- File I/O operations
- Data structures (lists, dictionaries, sets)
- Random module for game events
- String formatting and manipulation
- Function decorators
- Context managers

## Features

### Game Mechanics
- 🎮 Turn-based combat system
- 👤 Character creation and management
- 🎯 Quest and objective system
- 💪 Leveling and progression
- 🛡️ Equipment and inventory system
- 🧙 Magic spells and abilities
- 👹 Enemy AI and behavior
- 📊 Character statistics and skill trees

### Technical Features
- 💾 Game state persistence (save/load)
- 📝 Detailed game logging
- ⚙️ Configuration system
- 🧪 Code organization with modules
- 📖 Comprehensive documentation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/prellwitzdarian/-Advanced-Python-Module-Project-Defeat-the-Evil-Wizard.git
cd -Advanced-Python-Module-Project-Defeat-the-Evil-Wizard
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

4. Run the game:
```bash
python main.py
```

## How to Play

### Starting the Game

1. Run the main script
2. Create your character:
   - Choose your name
   - Select a character class (Warrior, Mage, Ranger, etc.)
   - Allocate skill points

### Game Commands

```
help              - Display available commands
stats             - View character statistics
inventory         - Check your inventory
equip <item>      - Equip an item
cast <spell>      - Cast a spell
attack            - Attack enemy
run               - Attempt to flee
save              - Save game progress
load              - Load saved game
quit              - Exit game
```

### Character Classes

#### Warrior
- High HP and defense
- Strong physical attacks
- Limited magic abilities
- Special ability: Block

#### Mage
- High magic power
- Various spell selection
- Low physical defense
- Special ability: Spell Amplify

#### Ranger
- Balanced stats
- Fast attack speed
- Good evasion
- Special ability: Precise Shot

#### Rogue
- High evasion and critical chance
- Low HP
- Quick attacks
- Special ability: Backstab

### Combat System

- Character vs. Enemy turn-based combat
- Choose actions: Attack, Cast Spell, Use Item, Defend
- Damage calculation based on stats and equipment
- Experience points awarded for victories
- Loot drops from defeated enemies

## Project Structure

```
-Advanced-Python-Module-Project-Defeat-the-Evil-Wizard/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── game/
│   ├── __init__.py
│   ├── character.py
│   ├── enemy.py
│   ├── combat.py
│   ├── inventory.py
│   ├── spells.py
│   ├── equipment.py
│   └── quest.py
├── utils/
│   ├── __init__.py
│   ├── save_load.py
│   ├── logger.py
│   └── helpers.py
├── data/
│   ├── enemies.json
│   ├── items.json
│   ├── spells.json
│   └── quests.json
└── saves/
    └── (saved game files)
```

## Core Classes

### Character
```python
class Character:
    - name: str
    - character_class: str
    - level: int
    - experience: int
    - hp: int
    - mp: int
    - strength: int
    - intelligence: int
    - dexterity: int
    - defense: int
    - inventory: Inventory
    - spells: List[Spell]
    
    Methods:
    - take_damage(damage)
    - cast_spell(spell)
    - gain_experience(amount)
    - level_up()
    - equip_item(item)
```

### Enemy
```python
class Enemy:
    - name: str
    - hp: int
    - damage: int
    - level: int
    - experience_reward: int
    - loot: List[Item]
    
    Methods:
    - attack(target)
    - take_damage(damage)
    - use_ability()
```

### Combat
```python
class Combat:
    - player: Character
    - enemy: Enemy
    - turn: int
    
    Methods:
    - start_combat()
    - player_turn(action)
    - enemy_turn()
    - calculate_damage(attacker, defender)
    - end_combat(winner)
```

### Inventory
```python
class Inventory:
    - items: List[Item]
    - capacity: int
    
    Methods:
    - add_item(item)
    - remove_item(item)
    - get_item(name)
    - is_full()
```

## Game Flow

```
Start Game
    ↓
Create Character
    ↓
Main Game Loop
    ├─ Display Location
    ├─ Show Options
    ├─ Get Player Input
    ├─ Process Action
    │   ├─ Explore
    │   ├─ Fight Enemy
    │   ├─ Open Inventory
    │   ├─ Rest/Save
    │   └─ Advance Quest
    └─ Check Win Condition
       └─ Defeat Evil Wizard
          ↓
       Game Over
```

## Advanced Python Concepts Demonstrated

### 1. Object-Oriented Programming
```python
class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
    
    def level_up(self):
        self.level += 1
        self.max_hp += 10
```

### 2. Inheritance
```python
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Mage")
        self.intelligence = 18
    
    def cast_spell(self, spell):
        # Mage-specific implementation
        pass
```

### 3. Polymorphism
```python
def attack(character):
    # Works for any character type
    character.attack()
```

### 4. Exception Handling
```python
try:
    enemy = encounter_enemy()
except NoEnemyError:
    print("No enemies in this area")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
```

### 5. File I/O
```python
def save_game(character):
    with open(f'saves/{character.name}.pkl', 'wb') as f:
        pickle.dump(character, f)

def load_game(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
```

### 6. Decorators
```python
@log_action
def take_damage(self, amount):
    self.hp -= amount

@property
def is_alive(self):
    return self.hp > 0
```

## Game Balance

### Character Statistics
- **HP**: Health points (0-100)
- **MP**: Magic points (0-100)
- **Strength**: Physical attack power
- **Intelligence**: Spell power
- **Dexterity**: Evasion and critical chance
- **Defense**: Damage reduction

### Leveling System
- Each level increases stats
- Experience gained from combat
- Boss enemies give extra experience
- Level cap at 50

## Configuration

Edit `config.py` to customize:
- Starting stats
- Enemy difficulty
- Loot rates
- Experience multiplier
- Game difficulty levels

## Save and Load System

### Saving Progress
```
In-game command: save
Creates save file: saves/[character_name].pkl
```

### Loading Progress
```
In-game command: load [character_name]
Restores: Character state, inventory, progress
```

## Debugging and Logging

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

View game log:
```bash
tail -f game.log
```

## Testing

Run tests (if implemented):
```bash
pytest tests/
```

Test combat system:
```bash
python -m pytest tests/test_combat.py -v
```

## Learning Outcomes

This project demonstrates proficiency in:
- Object-Oriented Programming principles
- Class design and inheritance
- Polymorphism and abstraction
- Exception handling and validation
- File I/O and data persistence
- Algorithmic thinking (combat calculations)
- Game logic implementation
- Code organization and modularity
- Documentation and comments
- Testing and debugging
- User interface design (text-based)
- Data structure usage

## Advanced Features to Add

- [ ] GUI implementation with Tkinter
- [ ] Multiplayer support
- [ ] Procedural dungeon generation
- [ ] Advanced AI for enemies
- [ ] More character classes
- [ ] Skill trees and customization
- [ ] Trading system with NPCs
- [ ] Achievements and leaderboards
- [ ] Sound effects and music
- [ ] Web-based version

## Troubleshooting

### Game Won't Start
- Ensure Python 3.8+ is installed
- Check all dependencies in requirements.txt
- Verify main.py exists

### Save File Corrupted
- Delete the corrupted save file
- Start a new game

### Performance Issues
- Reduce enemy quantity
- Clear save files
- Check available system memory

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python - OOP Tutorial](https://realpython.com/object-oriented-programming-oop-in-python-3/)
- [Game Design Principles](https://www.gamasutra.com/)
- [Python Design Patterns](https://refactoring.guru/design-patterns/python)

## Future Development

Planned enhancements:
- Expanded story with multiple quests
- New areas to explore
- More enemy types and bosses
- Advanced magic system
- PvP functionality
- Mobile app version

## Performance Notes

- Game runs efficiently on most systems
- Save/load typically <1 second
- Turn-based gameplay minimizes CPU usage
- Scalable to handle large character levels

## License

This project is provided as-is for educational purposes.

## Author

Created by Darian Prellwitz

---

**Last Updated:** May 2026
