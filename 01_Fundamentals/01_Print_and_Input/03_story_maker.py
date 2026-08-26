"""
Problem: Take multiple inputs from the user (noun, verb, place) and generate a short formatted story.
"""

print("--- Welcome to the Story Maker! ---")
character_name = input("Enter a character name: ")
superpower = input("Enter a superpower: ")
city_name = input("Enter a city name: ")

# Using f-strings to inject variables directly into the text
story = f"\nOnce upon a time in {city_name}, there lived a coder named {character_name}. " \
        f"They were known for their secret superpower: {superpower}! " \
        f"Whenever {city_name} was in trouble with bugs, {character_name} saved the day."

print(story)