import random

# Dictionary mappings
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get computer's choice
computer = random.choice([-1, 0, 1])

# Get user's choice with input validation
while True:
    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").strip().lower()
    if youstr in youDict:
        break
    else:
        print("Invalid choice. Please enter s, w, or g.")

# Get numeric value from dictionary
you = youDict[youstr]

# Output choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Determine the result
if computer == you:
    print("It's a draw")
elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You win!")
else:
    print("You lose!")