import random,os, time

count = 0
goal = 10
playerHP = 100
maxplayerHP = 100
RPGWeapons = ["Sword", "Rod", "Dagger"]
RPGClass = ["Warrior", "Mage", "Rogue"]
RPGWeaponDamage = [10,5,1]
RPGWeaponDefense = [5,2,15]
RPGChoice = [] 
RPGMobs = ["Slime","Big Slime","Small Red Slime"]
RPGMobsHP = [15,25,10]
RPGMobsDamage = [2,5,7]
Levels = [1,2,3]
dice = [0,1,2]
RPGMobsRunChance = [20,80,10]
PlayerRunChance = [25,15,90]
def rollDice():
    global diceValue
    diceValue = random.choice(dice)
    print(f"Rolled a {diceValue}")

def enemyRoll():
    global currentEnemyValue
    currentEnemyValue = random.choice(dice)

def main():
    print("RPG Game project 0.1v Alpha.")
    for count in range(len(RPGClass)):
        print(f"{count}.", RPGClass[count])
    choice = int(input("Pick a class: "))
    print("You have chosen", "class: ", RPGClass[choice], "\nYour starting weapon is: ", RPGWeapons[choice])
    currentPlayerHP = playerHP
    while True:
        playerChoice = input("What will you do? \nA. Proceed B. Use item \nC. Check Inventory. \nChoice: ")
        if (playerChoice == "A") or (playerChoice == "a"):
            rollDice()
            if (diceValue == 0):
                print("You feel ominous as you continue through the dungeon...")
                time.sleep(1)
                os.system("clear")
            if (diceValue == 1):
                print("You proceed to the dungeon...")
                time.sleep(1)
                os.system("clear")
            elif (diceValue == 2):
                #game current values here
                enemyRoll()
                currentWeapon = RPGWeapons[choice]
                currentWeaponDamage = RPGWeaponDamage[choice]
                currentPlayerDefense = RPGWeaponDefense[choice]
                currentEnemy = RPGMobs[currentEnemyValue]
                currentEnemyHP = RPGMobsHP[currentEnemyValue]
                currentMaxEnemyHP = RPGMobsHP[currentEnemyValue]
                currentEnemyDamage = RPGMobsDamage[currentEnemyValue]
                print(f"You encounter a {currentEnemy}!")
                while (currentPlayerHP > 0):
                    if (currentEnemyHP > 0):
                        pass
                        time.sleep(1)
                        os.system("clear")
                    else:
                        break
                    print(f"What will you do? \nYour HP: {currentPlayerHP}/{maxplayerHP} \n\n{currentEnemy} \nEnemy HP: {currentEnemyHP}/{currentMaxEnemyHP}")
                    playerMove = input("a. Attack \nb. Defend \nc. Run \nAnswer: ")
                    if (playerMove == "a"):
                        #attack mob here
                        currentEnemyHP = currentEnemyHP - currentWeaponDamage
                        currentPlayerHP = currentPlayerHP - currentEnemyDamage
                        print(f"You hit {currentEnemy} with your {currentWeapon} for {currentWeaponDamage} damage!")
                        print(f"{RPGClass[choice]} took a beating from enemy {currentEnemy} and sustained {currentEnemyDamage}!")
                        time.sleep(1)
                        os.system("clear")
                    elif (playerMove == "b") or (playerMove == "B"):
                        #implement defend system here here
                        reducedEnemyDamage = currentEnemyDamage - currentPlayerDefense
                        currentPlayerHP = currentPlayerHP - reducedEnemyDamage
                        print("You took a defensive stance!")
                        print(f"{RPGClass[choice]} took a beating from enemy {currentEnemy} and sustained {reducedEnemyDamage}!")
                        time.sleep(1)
                        os.system("clear")
                    elif (playerMove == "c") or (playerMove == "C"):
                        #implement item run system here
                        print(f"{RPGClass[choice]} tried to run and...")
                        if (PlayerRunChance >= RPGMobsRunChance):
                            print("Successfully ran away!")
                            time.sleep(1)
                            os.system("clear")
                            break
                        else:
                            print("failed to escape!")
                            time.sleep(1)
                            os.system("clear")
                if (currentPlayerHP < 1):
                    print("You are dead")
                    break
                elif (currentEnemyHP < 1):
                    print("You won!")
                    time.sleep(1)
                    os.system("clear")
        elif (playerChoice == "B") or (playerChoice == "b"):
            #implement using items here
            print("You're not holding any item with you!")
        elif (playerChoice == "C") or (playerChoice == "c"):
            #Check inventory
            print("You don't have a bag!")
            

if __name__ == "__main__":
    main()
