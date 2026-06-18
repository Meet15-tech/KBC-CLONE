import random
import time


# Save winner history
def save_history(name, amount, result):

    file = open("winner_history.txt", "a")

    file.write("\n====================\n")
    file.write("Name: " + name + "\n")
    file.write("Amount Won: " + amount + "\n")
    file.write("Result: " + result + "\n")

    file.close()


# Read Hot Seat player
file = open("hotseat.txt", "r")

player_data = file.readlines()

file.close()


name = player_data[0].replace("Name: ", "").strip()


print("\n======================================")
print("       KAUN BANEGA CROREPATI")
print("======================================")

print("\nDeviyon aur sajjano...")
print("Computer ji, hamare contestant")
print(name, "ko Hot Seat par bulaya jaye!")


# Read Questions
file = open("questions.txt", "r")

questions = file.readlines()

file.close()


# Read Options
file = open("options.txt", "r")

options = file.readlines()

file.close()


# Read Answers
file = open("answers.txt", "r")

answers = file.readlines()

file.close()


# Remove new lines
for i in range(len(questions)):

    questions[i] = questions[i].strip()

    options[i] = options[i].strip()

    answers[i] = answers[i].strip()


# Read FFF used question index
file = open("fff_used.txt", "r")

fff_question = int(file.read())

file.close()


# Create question pools according to difficulty

easy = list(range(0, 20))

moderate = list(range(20, 40))

hard = list(range(40, 60))

hardest = list(range(60, 80))

extreme = list(range(80, 90))

ultimate = list(range(90, 100)) 


# Remove FFF question from its level

if fff_question in easy:

    easy.remove(fff_question)

elif fff_question in moderate:

    moderate.remove(fff_question)

elif fff_question in hard:

    hard.remove(fff_question)

elif fff_question in hardest:

    hardest.remove(fff_question)

elif fff_question in extreme:

    extreme.remove(fff_question)

else:

    ultimate.remove(fff_question)


# Select questions level-wise

selected_questions = []


selected_questions += random.sample(easy, 3)

selected_questions += random.sample(moderate, 3)

selected_questions += random.sample(hard, 3)

selected_questions += random.sample(hardest, 3)

# Q13–Q15 (₹25 Lakh to ₹1 Crore)
selected_questions += random.sample(extreme, 3)

# Q16 (₹7 Crore)
selected_questions += random.sample(ultimate, 1)
# Money Ladder

money = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹1 Crore",
    "₹7 Crore"
]


# Starting amount
current_amount = "₹0"

# Safe amount
safe_amount = "₹0"


# Lifeline status

fifty_used = False
audience_used = False


# Start KBC Game

for i in range(16):

    index = selected_questions[i]


    print("\n========================================")
    print("Question", i + 1, "for", money[i])
    print("========================================")


    print("\nQuestion:")
    print(questions[index])


    print("\nOptions:")
    print(options[index])


    # Show available lifelines

    print("\n------------ Lifelines ------------")


    if not fifty_used:
        print("1. 50:50")


    if not audience_used:
        print("2. Audience Poll")


    if fifty_used and audience_used:
        print("No lifelines remaining.")


    print("-----------------------------------")


    # Ask for lifeline

    choice = input(
        "\nDo you want to use a lifeline? (yes/no): "
    ).lower()


    if choice == "yes":

        lifeline = input(
            "Enter 1 for 50:50 or 2 for Audience Poll: "
        )


        # 50:50 Lifeline

        if lifeline == "1":

            if fifty_used:

                print("\n50:50 Lifeline already used.")


            else:

                fifty_used = True


                option_letters = [
                    "A",
                    "B",
                    "C",
                    "D"
                ]


                option_letters.remove(answers[index])


                wrong_option = random.choice(option_letters)


                print("\n========================")
                print("       50:50 Result")
                print("========================")


                print(
                    "Remaining options:",
                    answers[index],
                    "and",
                    wrong_option
                )


        # Audience Poll Lifeline

        elif lifeline == "2":

            if audience_used:

                print("\nAudience Poll already used.")


            else:

                audience_used = True


                correct_vote = random.randint(50, 80)


                remaining = 100 - correct_vote


                votes = {
                    "A": 0,
                    "B": 0,
                    "C": 0,
                    "D": 0
                }


                votes[answers[index]] = correct_vote


                option_letters = [
                    "A",
                    "B",
                    "C",
                    "D"
                ]


                option_letters.remove(
                    answers[index]
                )


                vote1 = random.randint(
                    0,
                    remaining
                )


                vote2 = random.randint(
                    0,
                    remaining - vote1
                )


                vote3 = (
                    remaining - vote1 - vote2
                )


                votes[option_letters[0]] = vote1
                votes[option_letters[1]] = vote2
                votes[option_letters[2]] = vote3


                print(
                    "\n====== Audience Poll ======"
                )


                print(
                    "A:", votes["A"], "%"
                )

                print(
                    "B:", votes["B"], "%"
                )

                print(
                    "C:", votes["C"], "%"
                )

                print(
                    "D:", votes["D"], "%"
                )


        else:

            print(
                "\nInvalid Lifeline Choice."
            )
                # ---------------- Final Answer Section ----------------

    choice = input(
        "\nPress 1 to answer the question or 2 to quit the game: "
    )


    # Player quits the game

    if choice == "2":

        print("\nComputer ji...")

        print("Aapne khel chhodne ka faisla kiya hai.")

        print("Aap ghar lekar jayenge", current_amount)


        save_history(
            name,
            current_amount,
            "Quit"
        )

        break


    # Start answer timer

    start_time = time.time()


    # Answer validation

    while True:

        answer = input(
            "\nEnter your answer (A/B/C/D): "
        ).upper()


        if answer in [
            "A",
            "B",
            "C",
            "D"
        ]:

            break


        print(
            "Invalid answer! Please enter A, B, C or D."
        )


    end_time = time.time()


    time_taken = end_time - start_time


    print("\nComputer ji, is jawab ko lock kiya jaye!")

    print(
        "Time taken:",
        round(time_taken, 2),
        "seconds"
    )


    # Check timeout

    if time_taken > 30:

        print("\nSamay samapt ho gaya!")

        print(
            "Aapne 30 seconds se zyada samay liya."
        )

        print(
            "Aap ghar lekar jayenge",
            safe_amount
        )


        save_history(
            name,
            safe_amount,
            "Time Out"
        )

        break


    # ---------------- Correct Answer ----------------

    if answer == answers[index]:


        print("\nComputer ji...")

        print(
            "Aapka jawab bilkul sahi hai!"
        )


        current_amount = money[i]


        print(
            "Aap jeet chuke hain",
            current_amount
        )


        # Update safe amounts

        if i == 4:

            safe_amount = "₹10,000"


        elif i == 9:

            safe_amount = "₹3,20,000"


        print(
            "Current Safe Amount:",
            safe_amount
        )


    # ---------------- Wrong Answer ----------------

    else:


        print("\nAfsos...")

        print(
            "Yeh jawab galat hai."
        )


        print(
            "Sahi jawab tha:",
            answers[index]
        )


        print(
            "Aap ghar lekar jayenge",
            safe_amount
        )


        save_history(
            name,
            safe_amount,
            "Wrong Answer"
        )

        break



# ---------------- Winner Section ----------------

else:


    print("\n=====================================")

    print("Computer ji...")

    print("Deviyon aur sajjano...")

    print(
        "Bahut bahut badhai ho!"
    )

    print(
        "Aap ban chuke hain"
    )

    print(
        "🌟 ₹7 Crore ke Vijeta 🌟"
    )


    print("=====================================")


    save_history(
        name,
        "₹7 Crore",
        "Winner"
    )