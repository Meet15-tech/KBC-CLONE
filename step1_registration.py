import os


# Remove old player files
number = 1

while True:

    filename = "player" + str(number) + ".txt"

    if os.path.exists(filename):

        os.remove(filename)
        number += 1

    else:
        break


print("==========================================")
print("        KAUN BANEGA CROREPATI")
print("        Contestant Registration")
print("==========================================")


# Enter number of contestants
while True:

    total_players = input("Enter number of players (2-10): ")

    if total_players.isdigit():

        total_players = int(total_players)

        if total_players >= 2 and total_players <= 10:
            break

    print("Invalid number! Enter players between 2 and 10.")


# Register players
for i in range(1, total_players + 1):

    print("\n------------------------------------------")
    print("Player", i, "Registration")
    print("------------------------------------------")


    # Name validation
    while True:

        name = input("Enter your name: ").strip()

        if name.replace(" ", "").isalpha():

            break

        else:

            print("Invalid name! Enter letters only.")


    # Age validation
    while True:

        age = input("Enter your age: ")

        if age.isdigit():

            age_number = int(age)

            if age_number >= 10 and age_number <= 100:
                break

        print("Invalid age! Age must be between 10 and 100.")


    # City validation
    while True:

        city = input("Enter your city: ").strip()

        if city.replace(" ", "").isalpha():

            break

        else:

            print("Invalid city! Enter letters only.")


    # Create player file
    filename = "player" + str(i) + ".txt"

    file = open(filename, "w")

    file.write("Player Number: " + str(i) + "\n")
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("City: " + city + "\n")

    file.close()


    print("\nComputer ji, Player", i, "ki registration complete ki jaye!")
    print("Contestant", name, "is ready for KBC!")


# Save total number of players
file = open("total_players.txt", "w")

file.write(str(total_players))

file.close()


# Final KBC message
print("\n==========================================")
print("Deviyon aur sajjano...")
print("Hamare", total_players, "contestants taiyar hain!")
print("Ab shuru hoga Fastest Finger First Round!")
print("==========================================")
