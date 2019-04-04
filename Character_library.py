import random


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

    def check_inventory(self,check):
        if check == 'inv':
            print('Your inventory holds {}'.format(self.inventory))
            check = None
        return check

    def equip_weapon(self,item,weapon_directory):
        if self.weapon != None:
            self.damage = self.damage - weapon_directory[str(self.weapon)]['damage']
            self.inventory.append(self.weapon)
        self.weapon = item
        self.damage = self.damage + weapon_directory[str(self.weapon)]['damage']
        self.inventory.remove(item)


    def browse_monster_inventory(self,name,money,inventory):
        print('The ' + name + ' has ' + str(money) + ' gold and in its inventory there is {}'.format(inventory))
        choice = input('Would you like to pick it all up? yes or no?\n')
        if choice == 'yes':
            self.pick_up_all(money,inventory)
        elif choice == 'no':
            self.choose_from_items(money,inventory)

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
        print('added to inventory\n Your inventory now holds {}'.format(inventory))
        print('and you have {} gold'.format(self.money))






class Monster(Character):
    def __init__(self, name, health, damage, defense,inventory, money, money_range):
        super().__init__(name, health, damage, defense,inventory, money)
        self.inventory = [item for item in inventory if random.randint(0,1)%2 == 0]
        self.money = money + random.randint(0,money_range)


