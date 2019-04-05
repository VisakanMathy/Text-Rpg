import random
from item_library import *


class Character():
    def __init__(self, name, health, damage, defense,inventory, money):
        self.name = name
        self.defense =defense
        self.health = health
        self.damage = damage

class User(Character):

    def __init__(self, name, health, damage, defense,inventory, money,style):
        super().__init__(name, health, damage, defense,inventory, money)
        self.style = style
        self.weapon = None
        self.money = money
        self.inventory = inventory


    def check_inventory(self):
        items_to_remove = []
        print('Your inventory contains {}'.format(self.inventory))
        choice = input('would you like to browse your inventory yes or no?\n')
        if choice == 'yes':
            for item in self.inventory:
                if str(item) in item_directory.keys():
                    print(item +': ' + item_directory[str(item)]['description'])
                    choice = input('would you like to remove item yes or no? \n')
                    if choice == 'yes':
                        items_to_remove.append(item)
                        print('you have removed the item')
                elif str(item) in weapon_directory.keys():
                    print('{} is a {} with damage bonus of +{}'.format(item, weapon_directory[str(item)]['style'], weapon_directory[str(item)]['damage']))
                    if self.weapon != None:
                        print('Your {} has +{} damage'.format(self.weapon, weapon_directory[str(self.weapon)]['damage']))
                    choice = input('would you like to equip the {}'.format(item))
                    if choice == 'yes':
                        self.equip_weapon(item)
            if self.inventory == []:
                print('your inventory is empty')
            try:
                for item in items_to_remove:
                    self.inventory.remove(item)
            except ValueError:
                print('nothing was removed')
                pass


    def equip_weapon(self,item):
        if weapon_directory[str(item)]['style'] == self.style:
            if self.weapon != None:
                self.damage = self.damage - weapon_directory[str(self.weapon)]['damage']
                self.inventory.append(self.weapon)
            self.weapon = item
            self.damage = self.damage + weapon_directory[str(self.weapon)]['damage']
            self.inventory.remove(item)
            print('you now have {} damage'.format(self.damage))
        else:
            print('This item does not match your class')



    def browse_monster_inventory(self,name,money,inventory):
        choice = input("would you like to browse the {}'s belongings yes or no\n".format(name))
        if choice == 'yes':
            print('The ' + name + ' has ' + str(money) + ' gold and in its inventory there is {}'.format(inventory))
            choice = input('Would you like to pick it all up? yes or no?\n')
            if choice == 'yes':
                self.pick_up_all(money,inventory)
            elif choice == 'no':
                self.choose_from_items(money,inventory)
        elif choice == 'no':
            print('You didnt add anything\n')

        print('Your inventory now holds {}'.format(self.inventory))
        print('and you have {} gold'.format(self.money))

    def pick_up_all(self,money,inventory):
        self.money += money
        self.inventory = self.inventory + inventory

    def choose_from_items(self, money, inventory):
        choice = input('would you like to pick up the {} gold?\n'.format(money))
        if choice == 'yes':
            self.money += money
        for item in inventory:
            choice = input('would you like to pick up the {}?\n'.format(item))
            if choice == 'yes':
                self.inventory.append(item)
        print("that's everything")







class Monster(Character):
    def __init__(self, name, health, damage, defense,inventory, money, money_range):
        super().__init__(name, health, damage, defense,inventory, money)
        self.inventory = [item for item in inventory if random.randint(0,1)%2 == 0]
        self.money = money + random.randint(0,money_range)
