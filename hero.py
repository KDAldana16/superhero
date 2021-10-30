import random
import weapon import Weapon

random.randint(2, 7)

from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''

        name = input("What is the ability name?     ")
        max_damage = input(
            "What is the max damage of the ability?     ")

            return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        pass

    def create_armor(self):
        '''Prompt user for Armor information
            return Armor with values from user input.
        '''
        pass

    def create_hero(self):
        '''Prompt user for Hero information
            return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
            elif add_item == "2":
            elif add_item == "3":
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one'''
        numOfTeamMembers = int(input("How many members would you like in Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team two'''
        numOfTeamMembers2 = int(input("How many members would you like in Team Two?\n"))
        for i in range(numOfTeamMembers2):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def show_stats(self)
        ''prints team statistics to terminal''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was " + str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
    def fight(self, opponent):
        ''' Current Hero will take turn fighting the opponet hero passed in.
        '''
        pass

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attaacks.
            return: total_damage:Int
        '''
        total_damage = 0
            for ability in self.abilities:
                total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        pass

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.
        '''
        pass

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        pass

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''Update deaths with num_deaths'''
        pass

    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.deaths = 0
    self.kills = 0

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.current_health())
    print(hero.abilities)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)




class Ability:
    def __init__(self, name, max_damage):
        '''
        Initalize the values passed into this method as instance variables
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage.'''
        random_value = random.randint(0,self.max_damage)
        return random_value

    if __name__ == "__main":
        ability = Ability("Debugging Ability", 20)
        print(ability.name)
        print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in
        pass

    def block(self):
        '''return a random value between 0 and the initialized max_block strength.
        '''
        pass

    if __name__ == "__main__":
        armor = Armos("Debugging Shield", 10)
        print(armor.name)
        print(armor.block())

class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours {}".format(
                self.name,
                self.sleep_duration))

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

    my_dog = Dog("Sophie", 12)
    my_dog.sleep()
    my_dog.bark()

class Team:
    def __init__(self, name):
        '''Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''

        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

        def view_all_heroes(self):
            '''Prints out all heroes to the console.'''
            pass

        def add_hero(self, hero)
        ''Add Hero object to self.heroes''
        pass

        def stats(self):
            '''Print team statistics'''
            for hero in self.heroes:
                kd = hero.kills / hero.deaths
                print("{} Kill/Deaths:{}".format(hero.name,kd))

        def revive_heroes(self, health=100):
            '''Reset all heroes health to starting_health'''
            pass

        def attack(self, other_team):
            '''Battle each team against each other.'''

            living_heroes = list()
            living_opponents = list()

            for hero in self.heroes:
                living_heroes.append(hero)

            for hero in other_team.heroes:
                living_opponents.append(hero)

            while len(living_heroes) > 0 and len(living_opponents)> 0:
