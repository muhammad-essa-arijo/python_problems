"""
Problem: Demonstrate variable scope (Local vs Global) and how they occupy different memory spaces.
"""

# Global Variable (Exists throughout the program)
player_score = 100

def update_score():
    # Local Variable (Creates a new memory space inside the function, doesn't change the global one)
    player_score = 500
    print(f"Inside Function (Local): score is {player_score} | ID: {id(player_score)}")

update_score()

# The global variable remains unchanged because it has a different memory address
print(f"Outside Function (Global): score is {player_score} | ID: {id(player_score)}")