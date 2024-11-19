
# Module 8 Lab Activity - Booleans
# Author: Menhajudin
# Date: 2024-11-13

# Problem 1: Function to check if two inputs are equal
def p1(a, b):
    """
    This function takes two inputs and prints whether they are equal or not.
    """
    print("Equal" if a == b else "Not Equal")

# Problem 2: Function to compare the sum of two numbers with 10
def p2(a, b):
    """
    This function takes two inputs, sums them, and prints if the sum is greater than,
    less than, or equal to 10.
    """
    total = a + b
    if total > 10:
        print("Greater than 10")
    elif total < 10:
        print("Less than 10")
    else:
        print("Equal to 10")

# Problem 3: Function to check if 5 is in a list, implemented recursively for extra points
def p3(arr):
    """
    This function takes a list and checks if the value 5 is in that list, recursively.
    """
    if not arr:
        print("5 is not in the list")
        return
    if arr[0] == 5:
        print("5 is in the list")
    else:
        p3(arr[1:])

# Problem 4: Function to check if a year is a leap year
def p4(year):
    """
    This function takes a year as a parameter and returns True if it's a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Problem 5: Character class and task-checking functions
class Character:
    """
    This class represents a game character with a nickname, weapons, and weaknesses.
    """
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

# Example character with the given items and debuffs
player1 = Character(
    nickname="Dragon Slayer",
    weapons=["pan", "paper", "idea", "rope", "groceries"],
    weaknesses=["slow"]
)

# Task-checking function with detailed feedback
def check_task(task_name, required_items, forbidden_debuffs):
    """
    This function checks if the character has all items required for a task and does not
    have any forbidden debuffs. It provides detailed feedback on missing items or debuffs.
    """
    # Determine if required items are present
    missing_items = [item for item in required_items if item not in player1.weapons]
    # Check for forbidden debuffs
    active_debuffs = [debuff for debuff in forbidden_debuffs if debuff in player1.weaknesses]
    
    # Output result based on checks
    if not missing_items and not active_debuffs:
        print(f"{task_name}: Success")
    else:
        # Prepare failure message with details
        failure_message = f"{task_name}: Failure"
        if missing_items:
            failure_message += f" - Missing items: {', '.join(missing_items)}"
        if active_debuffs:
            failure_message += f"; Forbidden debuff(s): {', '.join(active_debuffs)}"
        print(failure_message)

# Running tasks with detailed feedback
check_task("Climb a mountain", ["rope", "coat", "first aid kit"], ["slow"])  # Expected: Failure, missing items and debuff
check_task("Cook a meal", ["pan", "groceries"], ["small"])                   # Expected: Success
check_task("Write a book", ["pen", "paper", "idea"], ["confusion"])          # Expected: Failure, missing item
