#RPG
import time
from Character_library import *
from item_library import *

file_read = open('username.txt', 'r')
usernames = eval(file_read.read())




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
                        print('your password was incorect')
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
                print(create_username + 'exists please try again')
                create_username = None
    else:
        print('{} is not a valid choice'.format(no_chosen_account))
        no_chosen_account = None


fight_class = None

inventory = []

while fight_class==None:
    fight_class = input("hello {}, let's now pick a style of fighting\n1) Melee\n2) Range \n3) Mage\n".format(username))
    if fight_class == '1' or fight_class.lower() == 'melee':
        print('you get a blunt stick')
        fight_class = 'melee'
        inventory.append('blunt stick')
    elif  fight_class == '2' or fight_class.lower() == 'range':
        print('you get a bag of rocks')
        fight_class = 'range'
        inventory.append('bag of rocks')
    elif fight_class == '3' or fight_class.lower() == 'mage':
        print('you get a stick')
        fight_class = 'mage'
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
    if choice == 'left':
        print('you encounter a fox')
        fox = Monster('fox',10,2,2,['fox meat','fur'],15,10)
        time.sleep(1)
        choice = input('Would you like to fight or ignore the fox\n')
        if choice == 'fight':
            print("you use use your hands to wrestle the fox")
            print('that was a difficult fight, you decide to equip your weapon from earlier')
            character.equip_weapon(inventory[0])
            character.browse_monster_inventory(fox.name,fox.money,fox.inventory)
        elif (choice == 'ignore'):
            print('The fox is ferocious and decides to chase and attack you and deals 5 damage to you')
            character.health -= 5
            time.sleep(1)
            print('you have {} health left'.format(character.health))
            time.sleep
            choice = input('Would you like to fight or run\n')
            if choice == 'fight':
                print('you punch the fox till it dies')
                time.sleep(1)
                print('that was a difficult fight, you decide to equip your weapon from earlier')
                character.equip_weapon(inventory[0])
                character.browse_monster_inventory(fox.name,fox.money,fox.inventory)
            elif(choice == 'run'):
                print('you manage to escape from harms way')
                print('you decide to equip your weapon to feel safer')
                character.equip_weapon(inventory[0])
    else:
        choice = None
        print('its a dead end')
        print('try left')

