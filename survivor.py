#static libraries and lists
import random
import os
occupations = ["Fire Fighter", "Police Officer", "Lumber Jack", "Unemployed", "Athelete"]
environments = ["City5", "Town3", "desert2", "Barren Plane1"]
items = ["crowbar3", "wrench2", "short pipe2", "base ball bat4", "hand-gun6", "bunch of hand-gun ammo1",
         "bandage1", "med-kit1"]
run_awayfail = "The monster caught up to you.You tripped as you attempted to run."
alive = True

class Person:
    inventory = []
    def __init__(self, name, age, occupation, health):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.health = health

#survivor
class Survivor(Person):
    def stats(self):
        print(f"""||{self.name}||
age: {self.age}
occupation: {self.occupation}
health: {self.health}/100""")
    def inventory(self):
        if len(Person.inventory) > 0:
            for i in Person.inventory:
                  print(i)
        else:
            print("Inventory is empty.")
    def attack(self):
        if len(Person.inventory) == 0:
            print("You punch the monster")
        else:
            choice = input(f"""{print(Person.inventory)}
What item do you want to use? """)

#monster            
class Monster(Person):
    def attack(self):
        if random.randrange(0,100) > 50:
            print("A monster has swung and harmed you")
            player.health -= random.randrange(0,65)
            if player.health() <= 0:
                alive = False
                print("You died.")
        else:
            print("A monster swung at you but missed.")
        
print("||SURVIVOR||")
name = input("Name: ")
player = Survivor(name, random.randrange(14, 120), random.choice(occupations), 70 + random.randrange(0, 30))

#gameplay
while alive:
    choice = input("command: ")
    os.system("cls")


    #help
    if choice == "help":
        print("""help - Bring up help menus
observe - Observe your current environment
move [direction] - Move in basic cardinal directions
stats - Display current statistics about your character
inventory - Display your inventory""")


#observe        
    elif choice == "observe":
        if item_avail == True:
            if monster == True:
                ranitem = random.choice(items)
                if random.randrange (0,120) > 50:
                     choice = input(f"""You identify a {ranitem} on the ground
and a monster standing... ominously.
do you [run], [fight] or [pickup] the object? """)
                     if choice == "run":
                         if random.randrange(0, 100) > 45:
                             print("You ran away successfully")
                             c_e = random.choice(list(environments))
                             c_e.split()
                             c_enum = c_e[-1]
                             c_enum = int(c_enum)
                             c_el = len(c_e)
                             print(f"You are in a {c_e[0:c_el-1]}.")
                             if random.randrange(0,85) > 50:
                                 monster = True
                             elif random.randrange(0, 40) * c_enum > 50:
                                 item_avail = True
                             else:
                                 item_avail = False
                         else:
                             if random.randrange(0,10) > 5:
                                 print(run_awayfail[0:28])
                             else:
                                 print(run_awayfail[29:-1])
                         m.attack()
                     elif choice == "fight":
                         player.attack()
                     elif choice == "pickup":
                         pass
                else:
                    print(f"""You identify a {ranitem}.
Do you pick this up?""")
                    choice = input("[yes/no]: ")
                    if choice == "yes":
                        m.attack()
                        Person.inventory.append(ranitem)
                        item_avail = False
                        choice = input("Do you [fight] the monster or [run]? ")
                        if choice == "run":
                             if random.randrange(0, 100) > 45:
                                 print("You ran away successfully")
                                 c_e = random.choice(list(environments))
                                 c_e.split()
                                 c_enum = c_e[-1]
                                 c_enum = int(c_enum)
                                 c_el = len(c_e)
                                 print(f"You are in a {c_e[0:c_el-1]}.")
                                 if random.randrange(0,85) > 50:
                                     monster = True
                                 elif random.randrange(0, 40) * c_enum > 50:
                                     item_avail = True
                                 else:
                                     item_avail = False
                             else:
                                 if random.randrange(0,10) > 5:
                                     print(run_awayfail[0:28])
                                     m.attack()
                                 else:
                                     print(run_awayfail[29:-1])
                                     m.attack()
                        if choice == "fight":
                            pass
                    elif choice == "no":
                        print("It becomes apparent that a monster is lurking near you.")
                    else:
                        print("The item was broken with your clumsy hands.")
                        print("It becomes apparent that a monster is lurking near you.")
        elif item_avail == True:
            ranitem = random.choice(items)
            print(f"""You identify a {ranitem}.
Do you pick this up?""")
            choice = input("[yes/no]: ")
            if choice == "yes":
                Person.inventory.append(ranitem)
                item_avail = False
            elif choice == "no":
                pass
            else:
                print("The item was broken with your clumsy hands.")
        else:
            print("Nothing seems to be here..")


#moving            
    elif "move" in choice:
        if choice.split()[1] in "northwestsoutheast":
            c_e = random.choice(list(environments))
            c_e.split()
            c_enum = c_e[-1]
            c_enum = int(c_enum)
            c_el = len(c_e)
            print(f"You are in a {c_e[0:c_el-1]}.")
            if random.randrange(0,85) > 50:
                monster = True
                m = Monster("monster", 3000, "monster", random.randrange(40, 100))
                if random.randrange(0, 40) * c_enum > 50:
                    item_avail = True
                else:
                    item_avail = False
            elif random.randrange(0, 40) * c_enum > 50:
                item_avail = True
            else:
                item_avail = False
            

#stats            
    elif choice == "stats":
        player.stats()
#inventory        
    elif choice == "inventory":
        player.inventory()
    else:
        print("Try typing 'help' to understand your commands.")
    

                 






        
