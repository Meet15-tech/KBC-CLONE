while True:

    print("\n================================")
    print("      KAUN BANEGA CROREPATI")
    print("================================")

    print("1. Register 8 Players")
    print("2. Fastest Finger First")
    print("3. Start KBC Game")
    print("4. View KBC Hall of Fame")
    print("5. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        exec(open("step1_registration.py").read())


    elif choice == "2":

        exec(open("step2_fastest_finger.py").read())


    elif choice == "3":

        print("\nDeviyon aur sajjano...")
        print("Swagat hai aapka Kaun Banega Crorepati mein!")

        exec(open("step3_kbc_game.py").read())


    elif choice == "4":

        exec(open("step8_leaderboard.py").read())


    elif choice == "5":

        print("\nDhanyavaad!")
        print("Milte hain agle episode mein KBC ke saath.")
        break


    else:

        print("Galat choice. Kripya dobara koshish karein.") 