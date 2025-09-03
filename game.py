import random
from paladin import Paladin
from hero import Hero

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Arthas Menethil")

    # Create paladins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    paladins = [Paladin(f"Knight of the Silver Hand {i+1}") for i in range(3)]

    # Keep track of how many paladins were defeated
    defeated_paladins = 0

    # Battle Loop 
    while hero.is_alive() and any(paladin.is_alive() for paladin in paladins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_paladin = random.choice([paladin for paladin in paladins if paladin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_paladin.name} for {damage} damage!")
        target_paladin.take_damage(damage)

        # Check if the target paladin was defeated
        if not target_paladin.is_alive():
            defeated_paladins += 1
            print(f"{target_paladin.name} has been defeated!")

        # paladins' turn to attack
        for paladin in paladins:
            if paladin.is_alive():
                damage = paladin.attack()
                print(f"{paladin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the paladins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of paladins defeated
    print(f"\nTotal paladins defeated: {defeated_paladins} / {len(paladins)}")

if __name__ == "__main__":
    main()
