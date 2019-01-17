#RPG
import time
import random


class Character():
    def __init__(self, name, health, damage, defense,inventory, money):
        self.name = name
        self.defense =defense
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.money = money
    

class User(Character):

    def __init__(self, name, health, damage, defense,inventory, money,style):
        super().__init__(name, health, damage, defense,inventory, money)
        self.style = style
        
    def check_inventory(self,check):
        if check == 'inv':
            print('Your inventory holds {}'.format(self.inventory))
            check = None
        return check    
        

file_read = open('username.txt', 'r')
usernames = eval(file_read.read())
print(usernames)

print('HELLO and WELCOME!')
no_chosen_account = None
while no_chosen_account==None:
    no_chosen_account = input("Do you have an account\n1)Yes \n2)No")
    if no_chosen_account == '1' or no_chosen_account.lower() == 'yes':
        username = None
        while username == None:
            username = input('Please type Your username')
            if username in usernames.keys():
                password = None
                while password == None:
                    password = input('Please type your password')
                    if password == usernames[username]['password']:
                        pass
                    else:
                        print('your password was incoreect')
                        password = None
            else:
                print('That username is invalid')
                username = None
    elif  no_chosen_account == '2' or no_chosen_account.lower() == 'no':
        
        create_username = None
        while create_username==None:
            create_username = input("To create an account type a username")
            if create_username not in usernames.keys():
                create_password = input('Write your password')
                usernames[create_username]= {'password': create_password}
                file_read.close()
                file_write = open('username.txt','w')
                file_write.write(str(usernames))
                file_write.close()
                username = create_username
    else:
        print('{} is not a valid choice'.format(no_chosen_account))
        no_chosen_account = None


fight_class = None

inventory = []





while fight_class==None:
    fight_class = input("hello {}, let's now pick a style of fighting\n1) Melee\n2) Range \n3) Mage\n".format(username))
    if fight_class == '1' or fight_class.lower() == 'melee':
        print('you get a blunt stick')
        inventory.append('blunt stick')
    elif  fight_class == '2' or fight_class.lower() == 'range':
        print('you get 10 rocks')
        inventory.append('10 rocks')
    elif fight_class == '3' or fight_class.lower() == 'mage':
        print('you get a stick')
        inventory.append('stick')
    else:
        print('{} is not a valid choice'.format(fight_class))
        fight_class = None
        
character = User(username,50,10,10,inventory,100,fight_class)
        
print('Time to begin you journey')
print('Would you like to follow the left path to forest or the right path into the town')
choice = None

while choice == None:
    choice = input('Type left or right\n')
    choice = character.check_inventory(choice)
    if choice == 'left':
        print('you encounter a fox')
        time.sleep(1)
        choice = input('Would you like to fight or ignore the fox\n')
        if choice == 'fight':
            print("you use {} to kill the fox".format(inventory[0]))
            choice = input('would you like to pick up the left over fox meat yes or no\n')
            if choice == 'yes':
                inventory.append('foxmeat')
                print('added fox meat to inventory\n Your inventory now holds {}'.format(inventory))
            elif choice == 'no':
                print('You didnt add anything\n you inventory now holds {}'.format(inventory))        
        elif (choice == 'ignore'):
            print('Thec fox is ferocious and decides to chase and attack you and deals 5 damage to you')
            health -= 5
            time.sleep(1)
            print('you have {} health left'.format(health))
            time.sleep
            choice = input('Would you like to fight or run\n')
            if choice == 'fight':
                print('you dismantle the fox with ease using {}'.format(inventory[0]))
                choice = input('would you like to pick up the left over fox meat yes or no\n')
                if choice == 'yes':
                    inventory.append('foxmeat')
                    print('added fox meat to inventory\n Your inventory now holds {}'.format(inventory))
                elif choice == 'no':
                    print('You didnt add anything\n you inventory now holds {}'.format(inventory))
                    
            elif(choice == 'run'):
                print('you manage to escape from harms way')
    elif choice == None:
        pass
    else:
        choice = None
        print('try left')
              
            
    
    