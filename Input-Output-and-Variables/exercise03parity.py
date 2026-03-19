"""
Exercise: 03 - Parity
Topic: Input, Output and Variables
Description:
    Identifies and prints if determined valid number is odd or even.
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
while True:
    UserNumber = input("\nPlease, enter the wanted number to check its parity:\n")
    if ValidateInput(UserNumber):
        UserNumber = int(UserNumber)
        break
    print("\nInvalid number, please try again.")

# Identifies the parity of the input number and prints the result
if UserNumber%2 == 0:
    print(f"{UserNumber} is even")
else:
    print(f"{UserNumber} is odd")