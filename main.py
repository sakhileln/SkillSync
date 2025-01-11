"""Main driver module."""

from helper import sign_in, sign_up

print("SkillSync")
choice = input("Do you have an account [Y/n]: ")
while choice not in ["", " ", "y", "Y", "n", "N"]:
    print("")
    print(f"Incorrect input: {choice}. Please try again..")
    choice = input("Do you have an account [Y/n]: ")

match choice.lower():
    case "" | " " | "y":
        print("Login option")
        sign_in()
    case "n":
        print("Sign up option")
        sign_up()
    case _:
        print("Invalid choice")