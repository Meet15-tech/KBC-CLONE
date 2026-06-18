import random
import time
import os


# Read questions file
file = open("questions.txt", "r")
questions = file.readlines()
file.close()


# Read options file
file = open("options.txt", "r")
options = file.readlines()
file.close()


# Read answers file
file = open("answers.txt", "r")
answers = file.readlines()
file.close()


# Remove extra spaces
for i in range(len(questions)):
    questions[i] = questions[i].strip()
    options[i] = options[i].strip()
    answers[i] = answers[i].strip()


# Find total registered players
total_players = 0

while True:

    filename = "player" + str(total_players + 1) + ".txt"

    if os.path.exists(filename):
        total_players += 1
    else:
        break


# Check players available or not
if total_players == 0:

    print("No contestants registered!")
    exit()


# Read player names
players = []

for i in range(1, total_players + 1):

    file = open("player" + str(i) + ".txt", "r")
    data = file.readlines()
    file.close()

    name = data[1].replace("Name: ", "").strip()

    players.append(name)


print("\n=================================================")
print("          KAUN BANEGA CROREPATI")
print("            Fastest Finger First")
print("=================================================")

print("\nDeviyon aur sajjano, swagat hai KBC mein!")
print("Computer ji, Fastest Finger First ka prashn screen par dikhaya jaye!")


# Select random question
index = random.randint(0, len(questions) - 1)


print("\nQuestion:")
print(questions[index])

print("\nOptions:")
print(options[index])


winner = ""
winner_name = ""
fastest_time = 999999


# Players answer one by one
for i in range(total_players):

    print("\n------------------------------------")
    print(players[i] + ", aapka jawab dijiye")
    print("------------------------------------")


    start = time.time()


    while True:

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer in ["A", "B", "C", "D"]:
            break

        print("Invalid option! Enter A, B, C or D.")


    end = time.time()

    total_time = end - start


    print("Answer Locked!")
    print("Time taken:", round(total_time, 2), "seconds")


    if answer == answers[index]:

        print("Correct Answer!")

        if total_time < fastest_time:

            fastest_time = total_time
            winner = "Player " + str(i + 1)
            winner_name = players[i]

    else:

        print("Wrong Answer!")


print("\n=================================================")
print("Computer ji, sabhi contestants ke jawab lock kiye jaye!")
print("=================================================")


# If winner found
if winner != "":

    print("\nAur sabse tez aur sahi jawab diya hai...")
    print("🏆", winner_name)
    print("Aap Hot Seat par pahunch gaye hain!")
    print("Aapka samay tha:", round(fastest_time, 2), "seconds")


    # Save hot seat player
    file = open("hotseat.txt", "w")

    file.write("Name: " + winner_name + "\n")
    file.write("Time: " + str(round(fastest_time, 2)))

    file.close()


    # Save used FFF question index
    file = open("fff_used.txt", "w")

    file.write(str(index))

    file.close()


else:

    print("\nKisi bhi contestant ne sahi jawab nahi diya.")