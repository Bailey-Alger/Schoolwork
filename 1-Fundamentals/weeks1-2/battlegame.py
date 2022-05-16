wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

print("1) Wizard")
print("2) Elf")
print("3) Human")

while True:
    character = int(input("Choose your character: "))
    if character == 1:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == 2:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == 3:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")

print("Your chosen character is:", character)
print("Your HP is:", my_hp)
print("Your damage is:", my_damage)
print()

while True:
    print("The", character, "damaged the Dragon!")
    dragon_hp -= my_damage
    print("The Dragon's HP is now:", dragon_hp)
    print()
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    my_hp -= dragon_damage
    print("The", character, "was attacked by the Dragon!")
    print("Your HP is now:", my_hp)
    print()
    if my_hp <= 0:
        print("The", character, "has lost the battle!")
        break
