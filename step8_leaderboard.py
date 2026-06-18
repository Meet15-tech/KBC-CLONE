print("========== KBC HALL OF FAME ==========")

try:

    file = open("winner_history.txt", "r")

    data = file.read()

    file.close()

    if data.strip() == "":
        print("No players have played KBC yet.")

    else:
        print(data)

except:

    print("No winner history found.")