"""
Exercise: 05 - Approvation
Topic: Input, Output and Variables
Description:
    Checks if determined grade is enough to the goal or not, that it can be numeric or letter-based grades
"""

def ValidateInput(InputNumber):
    """
    Validates if the input is a integer number

    Args:
        InputNumber(int): User input
    
    Return:
        bool: True if it's a valid integer number, False otherwise
    """
    
    try:
        InputNumber = int(InputNumber)
    except ValueError:
        # Handles non-integers numbers to prevent the program crash
        return False
    return True

# Repeats until the user provides a valid integer number
NumericGrade = input("\nEnter \"False\" if you don't want to use letters as grade\n")
while True:
    RequiredGrade = input("\nPlease, enter the required grade to approvation:\n")
    if ValidateInput(RequiredGrade):
        RequiredGrade = int(RequiredGrade)
        break
    print("\nInvalid number, please try again.")

if not NumericGrade:
    print("ok")