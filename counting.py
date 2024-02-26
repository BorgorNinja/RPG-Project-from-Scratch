import random

count = 0
goal = 10

RPGWeapons = ["Sword", "Rod", "Shield"]
RPGClass = ["Warrior", "Mage", "Paladin"]
RPGWeaponDamage = [10,5,1]
RPGWeaponDefense = [5,2,15]
RPGChoice = [] 
RPGMobs = ["Slime","Big Slime","Red Slime"]
Levels = [1,2,3]
dice = [1,2,3,4]
def rollDice():
    global diceValue
    diceValue = random.choice(dice)
    print(f"Rolled a {diceValue}")

def main():
    print("RPG Game project 0.1v Alpha.")
    for count in range(len(RPGClass)):
        print(f"{count}.", RPGClass[count])
    choice = int(input("Pick a class: "))
    try:
        print("You have chosen", "class: ", RPGClass[choice], "\nYour starting weapon is: ", RPGWeapons[choice])
        while True:
            playerChoice = input("What will you do? \nA. Proceed B. Use item \nC. Check Inventory.")
            if (playerChoice == "A"):
                rollDice()
                if (diceValue == 1):
                    print("You proceed to the dungeon...")
                elif (diceValue == 2):
                    currentEnemy = RPGMobs[1]
                    print(f"You encounter a {currentEnemy}!")
                    while True:
                        #this thing is still under implementation
                        print(f"What will you do? \nYour HP 100/100 \n{currentEnemy} HP ")  
                
                

    except:
        print("Class not found.")

if __name__ == "__main__":
    main()