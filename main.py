print("SkillSync")
choice = input("Do you have an account [Y/n]: ")
while choice not in ["", " ", "y", "Y", "n", "N"]:
    print("")
    print(f"Incorrect input: {choice}. Please try again..")
    choice = input("Do you have an account [Y/n]: ")

match choice.lower():
    case "" | " " | "y":
        print("Login option")
    case "n":
        print("Sign up option")
    case _:
        print("Invalid choice")